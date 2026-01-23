
$(document).ready(function() {

    async function load_text_and_initialize_interactive_elements() {

        const text_data = await fetch('text-it.json');
        try {
            var emotions_data_object = await text_data.json();
        }
        catch(_) {
            escape_and_revert_to_static_webapp('Error in JSON file');
        }

        $('#content').hide();
        $('#placeholder-container').show();

        Object.keys(emotions_data_object).forEach(function(emotion){
            var selected_emotion = emotions_data_object[emotion]

            $('.' + emotion).click(function(){
                console.log(emotion);
                console.log(selected_emotion);
                $('#content').hide();

                $('#placeholder-container').hide();
                // Stop the in-out animation
                $('.animate-at-start').each(function() {
                    $(this).one('animationiteration webkitAnimationIteration', function() {
                        $(this).removeClass('animate-at-start');
                    })
                })

                $('#content').hide();
                $('.emotion-name').text(capitalization_helper(emotion));
                ['similar-words', 'sensations', 'message', 'purpose'].forEach(function(param_name){
                    if (param_name in selected_emotion) {
                        $('#' + param_name + '-line').show()
                        $('#' + param_name).text(selected_emotion[param_name])
                    }
                    else {
                        $('#' + param_name + '-line').hide()
                    }
                });

                if (is_base_emotion(selected_emotion)) {

                    $('#base-emotion-explore-container').show();
                    $('#intermediate-emotion-explore-container').hide();

                    $('#emotion-title').css('background-color', selected_emotion['petal-color']);
                    // $('#emotion-title').removeClass('intermediate');
                    $('#intensity').text(selected_emotion['intensity']);

                    opposite = selected_emotion['opposite'];
                    $('#opposite-button').css('background-color', emotions_data_object[opposite]['color']);
                    $('#opposite-button').text(capitalization_helper(opposite));


                    if ('+intense' in selected_emotion) {
                        $('.increase-intensity').addClass('enabled');
                        $('.increase-intensity > .explore-arrow').css('fill', emotions_data_object[selected_emotion['+intense']]['color'])
                        up = selected_emotion['+intense'];
                    }
                    else {
                        $('.increase-intensity').removeClass('enabled');
                        $('.increase-intensity > .explore-arrow').css('fill', '#D3D3D3')
                        up = null;
                    }
                    if ('-intense' in selected_emotion) {
                        $('.decrease-intensity').addClass('enabled');
                        $('.decrease-intensity > .explore-arrow').css('fill', emotions_data_object[selected_emotion['-intense']]['color'])
                        down = selected_emotion['-intense'];
                    }
                    else {
                        $('.decrease-intensity').removeClass('enabled');
                        $('.decrease-intensity > .explore-arrow').css('fill', '#D3D3D3')
                        down = null;
                    }

                }

                else if (is_intermediate_emotion(selected_emotion)) {

                    $('#base-emotion-explore-container').hide();
                    $('#intermediate-emotion-explore-container').show();

                    $('#emotion-title').css('background-color', selected_emotion['color']);
                    // $('#emotion-title').addClass('intermediate');

                    ['combo-emotion-0', 'combo-emotion-1'].forEach(function(param){
                        try {
                            var combo_emotion = selected_emotion[param];
                            $('#' + param + '-button').text(capitalization_helper(combo_emotion));
                            combo_emotion_color = emotions_data_object[combo_emotion]['color'];
                            $('#' + param + '-button').css('background-color', combo_emotion_color);
                        }
                        catch {
                            escape_and_revert_to_static_webapp('Error populating combo emotion' + first_combo_emotion)
                        }
                    });

                    combo_0 = selected_emotion['combo-emotion-0'];
                    combo_1 = selected_emotion['combo-emotion-1'];

                    $('#combo-explanation').text(selected_emotion['combo-explanation']);

                }

                else {
                    escape_and_revert_to_static_webapp('Properties for ' + emotion + ' not properly defined')
                }

                $('#content').show();
            })

            if (is_intermediate_emotion(selected_emotion)) {
                $('.intermediate-emotion-container.' + emotion).hover(function(){
                    $('.intermediate-letter', this).css({fill: selected_emotion['color']})
                },
                function(){
                    $('.intermediate-letter', this).css({fill: ''})
                })
            }
        })

        function escape_and_revert_to_static_webapp(message){
            // TODO: Make this look better: Prevent hover stuff, center.
            // Turns dynamic webapp into static webapp
            $('.words').hide();
            // Stop the in-out animation, if it's still going
            $('.animate-at-start').each(function() {
                $(this).one('animationiteration webkitAnimationIteration', function() {
                    $(this).removeClass('animate-at-start');
                })
            });
            throw message;
        }

        function is_base_emotion(selected_emotion) {
            return ['intensity', 'opposite'].every(function(keyword){return keyword in selected_emotion});
        }

        function is_intermediate_emotion(selected_emotion) {
            return ['combo-emotion-0', 'combo-emotion-1', 'combo-explanation'].every(function(keyword){return keyword in selected_emotion});
        }
    };

    var up, down, opposite, combo_0, combo_1;

    load_text_and_initialize_interactive_elements();

    $('#opposite-button').click(function(){
        if (opposite != null) {
            $('.petal-shape.' + opposite).click();
        }
    });
    $('.increase-intensity').click(function(){
        if (up != null) {
            $('.petal-shape.' + up).click();
        }
    });
    $('.decrease-intensity').click(function(){
        if (down != null) {
            $('.petal-shape.' + down).click();
        }
    });
    $('#combo-emotion-0-button').click(function(){
        if (combo_0 != null) {
            $('.petal-shape.' + combo_0).click();
        }
    });
    $('#combo-emotion-1-button').click(function(){
        if (combo_1 != null) {
            $('.petal-shape.' + combo_1).click();
        }
    })

})

function capitalization_helper(word){
    return word.charAt(0).toUpperCase() + word.slice(1);
}
