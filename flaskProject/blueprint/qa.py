from flask import Blueprint, render_template, request, url_for, g, redirect
from .forms import QuestionForm, AnswerForm
from models import QuestionModel, AnswerModel
from exts import db
from decorators import login_required


# user management
# index page
bp = Blueprint("qa", __name__, url_prefix="/")


@bp.route("/")
def index():
    return render_template("chatapp.html")


@bp.route("/window")
def window():
    return render_template("window.html")

@bp.route("/qa/public", methods=['GET', 'POST'])
@login_required
def public_question():
    if request.method == 'GET':
        return render_template("question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for("qa.public_question"))


@bp.route("/history")
def history():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template("history.html", questions=questions)



@bp.route("/qa/detail/<qa_id>")
def qa_detail(qa_id):
    question = QuestionModel.query.get(qa_id)
    return render_template("detail.html", question=question)


@bp.route("/answer/public", methods=['POST'])
@login_required
def public_answer():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content=content, question_id=question_id, author_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("qa.qa_detail", qa_id=question_id))
    else:
        print(form.errors)
        return redirect(url_for("qa.qa_detail", qa_id=request.form.get("question_id")))

@bp.route("search")
def search():
    q = request.args.get("q")
    questions = QuestionModel.query.filter(QuestionModel.title.contains(q)).all()
    return render_template("history.html", questions=questions)










