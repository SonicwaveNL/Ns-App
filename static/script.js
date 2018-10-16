$(document).ready(function() {
    bindStationClick();
    bindReturnClick();
    bindSearch();
});

    function bindStationClick() {
        $(".station").click(function(event) {
            event.preventDefault();
            updateContent(this);
            $("ul li").css("display", "list-item");
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
            $(".wrap").html(data).promise().done(function() {
                bindReturnClick();
                bindSearch();
            });
        });
    }

    function bindSearch() {
        $(".search-station").on("keyup", function() {
            var value = $(this).val().toLowerCase();
            $("ul li").filter(function() {
              $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
          });
    }