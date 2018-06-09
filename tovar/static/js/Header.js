
jQuery(document).ready(function ($) {

    $('#src').submit(function (e) {
        e.preventDefault();
        var data = $(this).serialize();
        name_N = $('#ser').val();
        $('.load_start').addClass("d-block");

        $.ajax({
            type: "GET",
            url: "/games/src/",
            data: {'ser': name_N},
            cache: false,
            success: function (data) {
                // if (data == "yea") window.location = '/';
                $('.load_start').removeClass("d-block");
                if (data == "no"){
                    alert("Такой игры нет");
                }
                else $('body').html(data);

            }
        });
    });
    $('#sro').submit(function (e) {
        e.preventDefault();
        if ($('#pr').prop('checked')) list['1'] = '1';
        if ($('#vd').prop('checked')) list['2'] = '1';
        if ($('#op').prop('checked')) list['3'] = '1';
        if ($('#mt').prop('checked')) list['4'] = '1';
        $('#list1').val(list["1"]);
        $('#list2').val(list["2"]);
        $('#list3').val(list["3"]);
        $('#list4').val(list["4"]);
        GPU = $('#GpuList').val();
        $('#sel1').val(GPU);
        GPU = $('#OpList').val();
        $('#sel2').val(GPU);
        GPU = $('#ATX_List').val();
        $('#sel3').val(GPU);
        GPU = $('#soket_list').val();
        $('#sel4').val(GPU);
        GPU = $('#oper_List').val();
        $('#sel5').val(GPU);
        GPU = $('#DDR_List').val();
        $('#sel6').val(GPU);
        GPU = $('#soket_list2').val();
        $('#sel7').val(GPU);
        GPU = $('#core_list').val();
        $('#sel8').val(GPU);
        // alert("dd")
        // alert($('#sel1').val());
        var data = $(this).serialize();
        name_N = $('#ser').val();
        $('.load_start').addClass("d-block");
        $.ajax({
            type: "POST",
            url: "/src/",
            data: data,
            cache: false,
            success: function (data) {
                // alert(data);
                // if (data == "yea") window.location = '/';
                $('.load_start').removeClass("d-block");
                $('body').html(data);

            }
        });
    });
});

if (window.location.pathname !== '/') { $('#gl').removeClass('active');}
if (window.location.pathname.indexOf("games") !== -1) { $('#gl, #me').removeClass('active'); $('#gm').addClass('active');}
if (window.location.pathname.indexOf("my") !== -1) { $('#gl, #me, #me').removeClass('active'); $('#me').addClass('active');}
list = {'1': '0', '2': '0', '3': '0', '4': '0'};

function get_my_search(href) {

}

function podrobnee(str, str2) {
    // alert(st);
    id_ = str;
    $('.load_start').addClass("d-block");
    obj = str2;
    $.ajax({
        type: "GET",
        url: "/more/",
        data: {'id': id_, 'obj': obj},
        cache: false,
        success: function (data) {
            $('body').html(data);
        }
    });

}

function poisk_(id, its){
    // alert(list[id]);
    if (its === '11'){
        if ($('#pr').prop('checked')) list['1'] = '1';
        if ($('#vd').prop('checked')) list['2'] = '1';
        if ($('#op').prop('checked')) list['3'] = '1';
        if ($('#mt').prop('checked')) list['4'] = '1';
        return;
    }
    if (id === '1') {
        if (list[id] === '0'){
            $('#c1').addClass('card_cat_ac');
            list[id] = '1';
        }
        else {
            $('#c1').removeClass('card_cat_ac');
            list[id] = '0';
        }
    }
    else if (id == '2'){
        if (list[id] == '0'){
            $('#c2').addClass('card_cat_ac');
            list[id] = '1';
        }
        else {
            $('#c2').removeClass('card_cat_ac');
            list[id] = '0';
        }
    }
    else if (id == '3'){
        if (list[id] == '0'){
        $('#c3').addClass('card_cat_ac');
            list[id] = '1';

        }
        else {
            $('#c3').removeClass('card_cat_ac');
                list[id] = '0';

        }
    }
    else if (id == '4'){
        if (list[id] == '0'){
        $('#c4').addClass('card_cat_ac');
            list[id] = '1';
        }
        else {
            $('#c4').removeClass('card_cat_ac');
                list[id] = '0';

        }
    }

}

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
