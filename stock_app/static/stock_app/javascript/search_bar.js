function search_stocks(event) {
    // Get current text from input
    // Format text to remove spaces
    // Set as search_url

    $result_list = $('#results');
    $input_text = $('#search_box').val();
    formatted_input = encodeURIComponent($input_text.trim());
    search_url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + formatted_input + '&region=1&lang=en'//&callback=YAHOO.Finance.SymbolSuggest.ssCallback';
    exchanges = ['BZX', 'BYX', 'BOX',
                    'C2', 'CBOE', 'CHX',
                    'EDGA', 'EDGX',
                    'IEX', 'ISE', 'MIAX',
                    'NASDAQ', 'BX', 'PHLX',
                    'NSX', 'NYSE', 'NYSE ARCA', 'NYSE MKT']

    /*$result_list.empty();
    $result_list.append('<li><a href="#">' + search_url + '</a></li>');*/

    $.ajax({
        type: 'GET',
        url: search_url,
        jsonp: 'callback',
        dataType: 'jsonp',
        //jsonpCallback: "YAHOO.Finance.SymbolSuggest.ssCallback",
        success: function(data) {

            $result_list.empty();
            $.each(data['ResultSet']['Result'], function(key, obj){
                if ($.inArray(obj['exchDisp'], exchanges) !== -1) {
                    $result_list.append('<li><a href="/stock/' + obj['symbol'] + '">' + obj['symbol'] +
                        ': ' + obj['name'] + '</a></li>');
                    };
                });
            },
        error: function(data) {
            console.log("There was an error.")
            console.log(data)
        }
    });
}