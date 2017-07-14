function search_stocks(event) {
    // Get current text from input
    // Format text to remove spaces
    // Set as search_url

    $result_list = $('#results');
    $input_text = $('#search_box').val();
    formatted_input = encodeURIComponent($input_text.trim());
    formatted_url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + formatted_input + '&region=1&lang=en'//&callback=YAHOO.Finance.SymbolSuggest.ssCallback';
    exchanges = ['BZX', 'BYX', 'BOX',
                    'C2', 'CBOE', 'CHX',
                    'EDGA', 'EDGX',
                    'IEX', 'ISE', 'MIAX',
                    'NASDAQ', 'BX', 'PHLX',
                    'NSX', 'NYSE', 'NYSE ARCA', 'NYSE MKT']

    $.ajax({
        type: 'GET',
        url: '/api',
        //jsonp: 'callback',
        //dataType: 'jsonp',
        data: {
            search_url: formatted_url,
        },
        //jsonpCallback: "YAHOO.Finance.SymbolSuggest.ssCallback",

        success: function(response) {
            $result_list.empty();

            if (response['Result']) {
                $.each(response['Result'], function (key, stock) {
                    $result_list.append('<li><a href="/stock/' + stock['symbol'] + '">' + stock['symbol'] +
                        ': ' + stock['name'] + '</a></li>');
                })
            }
            else {
                $result_list.append('<li><a href="#">No search results found.</a></li>');
            }
            console.log(response)
        },
        /*success: function(data) {

            $result_list.empty();
            $.each(data['Result'], function(key, obj){
                if ($.inArray(obj['exchDisp'], exchanges) !== -1) {
                    $result_list.append('<li><a href="/stock/' + obj['symbol'] + '">' + obj['symbol'] +
                        ': ' + obj['name'] + '</a></li>');
                    };
                });
                else if $
            },*/
        error: function(response) {
            console.log("There was an error in the AJAX call.")
            console.log(response)
        }
    });
}