function setCookie(key, value) {
    var expires = new Date();
    expires.setTime(expires.getTime() + (24 * 3600 * 365))
    document.cookie = key + '=' + value + ';expires=' + expires.toUTCString();
}

function getCookie(key) {
    var keyValue = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
    return keyValue ? keyValue[2] : null;
}

(function () {
    $('select').niceSelect();

    if (getCookie('theme') === 'dark') {
        $('body').addClass('dark-theme');
    }
})();

$('#send').click(function (event) {
    event = event || window.event;

    $('#status-out').html('Sending...');

    var request = $.ajax({
        data: {
            bot_id: encodeURIComponent(
                $('#bot_id').children('option:selected').val()),
            user_id: encodeURIComponent(
                $('#user_id').children('option:selected').val()),
            text: encodeURIComponent($('#message')[0].value),
        },
        method: 'POST',
        url: '/send',
    });

    request.done(function (response) {
        $('#status-out').html(response.successful ? 'Successful' : response.reason);
    });

    request.fail(function (jqueryXHR, textStatus) {
        $('#status-out').html('Unknown error');
    });
});

$('#theme-button').click(function (event) {
    event = event || window.event;

    $('body').addClass('no-transition');
    $('body').toggleClass('dark-theme');

    setCookie('theme', $('body').hasClass('dark-theme') ? 'dark' : 'light');

    setTimeout(function () {
        $('body').removeClass('no-transition');
    }, 100);
});

$('#logout-button').click(function (event) {
    location.href = 'logout';
});

$('#admin-link').click(function (event) {
    location.href = 'admin';
});