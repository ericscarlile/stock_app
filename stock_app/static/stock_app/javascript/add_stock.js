var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function add_stock(stock_symbol) {

    $.ajax({
        type:"POST",
        data: {
            action: "add_stock",
            symbol: stock_symbol,
        },
        success: function(data) {
            $('#test').empty();
            $('#test').text(data.success);
        }
    });
}