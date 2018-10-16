$(document).ready(function() {
    bindStationClick();
    bindReturnClick();
});

    function bindStationClick() {
        $(".station").click(function(event) {
            event.preventDefault();
            updateContent(this);
    });
    }

    function bindReturnClick() {
        $(".back-button-link").click(function(event) {
            event.preventDefault();
            updateContent(this);
        });
    }

    function updateContent(target) {
        $.ajax({
          url: target.href,
        }).done(function(response) {
            data = $(response).find(".main");
            $(".main").html(data).promise().done(function() {
                bindReturnClick();
            });
        });
    }