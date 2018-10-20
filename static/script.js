$(document).ready(function() {
    bindStationClick();
    bindReturnClick();
    bindSearch();
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
        searchValue = $(".search-station").val();
        $(".home__wrapper, .content__wrapper").html("<div class='spinner__wrapper'><i class='fas fa-sync fa-spin'></i></div>");

        $.ajax({
          url: target.href,
        }).done(function(response) {
            data = $(response).find(".main");
            $(".wrap").html(data).promise().done(function() {
                $(".search-station").val(searchValue);
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