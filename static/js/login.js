jQuery(document).ready(function ($) {
    $('#formReg').submit(function (e) {
        e.preventDefault();
        var data = $(this).serialize();
        $('.load_start').addClass("d-block");
        $.ajax({
            type: "GET",
            url: "/auth/register/",
            data: data,
            cache: false,
            success: function (data) {
                if (data == "yea") window.location = '/';
                if (data.length > 100) $('header').replaceWith(data);
                else {
                    str = data;
                    if (data == "username") str = "Некорректный логин";
                    if (data == "password2username" || data == "password1password2username" || data == "usernamepassword2") str = "Некорректный логин и пароль";
                    if (data == "password1password2") str = "Некорректный пароль";
                    if (data == "password1" || data == "password2") str = "Не совпадают пароли";
                    $('#error-login').html(str);
                }
                $('.load_start').removeClass("d-block");
            }
        });
    });
    $('#formVhod').submit(function (e) {
        e.preventDefault();
        $('.load_start').addClass("d-block");
        var data = $(this).serialize();
        $.ajax({
            type: "GET",
            url: "/my/login/",
            data: data,
            cache: false,
            success: function (data) {
                if (data == "non") {
                    $('.load_start').removeClass("d-block");
                    $('#error-login').html("Неверный логин/пароль!");
                }
                else window.location = '/'
            }
        });
    });


});
