function bindEmailCaptchaClick(){
    $("#captcha-btn").click(function (event) {
        var $this = $(this);
        event.preventDefault();
        // prevent default events
        var email = $("#InputEmail").val();
        $.ajax({
            url: "/auth/captcha/email?email="+email,
            method: "GET",
            success: function (result){
                var code = result['code'];
                if (code == 200){
                    var countdown = 60;
                    $this.off("click")
                    var timer = setInterval(function (){
                        $this.text(countdown+"s")
                        countdown -= 1;
                        if (countdown<=0){
                            clearInterval(timer);
                            $this.text("Get Code");
                            bindEmailCaptchaClick();
                        }
                    }, 1000);
                }else{
                    alert("please type in a vaild email!");
                }
            },
            fail: function (error){
                alert("please type in a vaild email!");
            }
        })
    })
}





$(function () {
    bindEmailCaptchaClick();
})