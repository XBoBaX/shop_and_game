function go_game(id) {
    $('.load_start').addClass("d-block");
    $.ajax({
        type: "GET",
        url: "/games/select/",
        data: {'id': id},
        cache: false,
        success: function (data) {
            $('.load_start').removeClass("d-block");
            $('body').html(data);
        }
    });
}



$('#max').click(function () {
    id = $('#sekret').html();
    $('.load_start').addClass("d-block");

   $.ajax({
        type: "GET",
        url: "buy/",
        data: {'id': id, 'minORmax': 1},
        cache: false,
        success: function (data) {
            $('.load_start').removeClass("d-block");
            $('body').html(data);
        }
    });
});

$('#min').click(function () {
    id = $('#sekret').html();
    $('.load_start').addClass("d-block");

   $.ajax({
        type: "GET",
        url: "buy/",
        data: {'id': id, 'minORmax': 0},
        cache: false,
        success: function (data) {
            // alert(data)
            $('.load_start').removeClass("d-block");
            $('body').html(data);
        }
    });
});