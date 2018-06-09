if (window.location.pathname !== '/') { $('#gl').removeClass('active');}
if (window.location.pathname.indexOf("games") !== -1) { $('#gl, #me').removeClass('active'); $('#gm').addClass('active');}
if (window.location.pathname.indexOf("my") !== -1) { $('#gl, #me, #me').removeClass('active'); $('#me').addClass('active');}


$(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() != 0) {
            $('#toTop').fadeIn();
        } else {
            $('#toTop').fadeOut();
        }
    });
    $('#toTop').click(function () {
        $('body,html').animate({scrollTop: 0}, 800);
    });
});

function set_active(objName) {
    $('#gl, #gm, #me').removeClass('active');
    $(objName).addClass('active');

    if ($('#gl').hasClass('active')) window.location = '/';
    if ($('#gm').hasClass('active')) window.location.href = '/games/';
    // if ($('#me').hasClass('active')) window.location.href = '/my/';
}

$('#cl').click(function () {
    if ($('#poisk').css('height') == "60px" ||
        $('#poisk').css('height') == 60) {
        $('#poisk').animate({ //выбираем класс menu и метод animate
            height: 0,
            top: 0
        }, 200);
        $('#opCl').html('Поиск')
    }
    else {
        $('#poisk').animate({ //выбираем класс menu и метод animate
            height: 60,
            top: 0
        }, 200);
        $('#opCl').html('Скрыть')
    }

});