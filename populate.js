function populate() {
    $.getJSON('sampledata.json?' + Math.floor(Math.random()*30000), function (data) {
        var x = "";

        for (var category in data.alive) {
            x += "<div class=\"row align-row\">";

            x += "<h4>" + category + "</h4>";
            for (var entry in data.alive[category]) {
                x += "<span class=\"btn btn-success btn-override\">" +
                    entry + "<em>" + data['alive'][category][entry] + "</em></span>";
            }
            x += "</div>"
        }

        $('#alive-data').html(x);

        var x = "";

        for (var category in data.dead) {
            x += "<div class=\"row align-row\">";

            x += "<h4>" + category + "</h4>";
            for (var entry in data.dead[category]) {
                x += "<span class=\"btn btn-danger btn-override\">" +
                    data.dead[category][entry] + "</span>";
            }
            x += "</div>"
        }

        $('#dead-data').html(x);
    });
}

$(document).ready(function () {
    window.setInterval(populate, 3000);
    populate();
});
