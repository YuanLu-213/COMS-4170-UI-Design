function validation(input){
    if (input.replace(/\s+/g, "").length == 0){
        return false;
    }
    return true;
}

$(document).ready(function(){
    $("#search").autocomplete({
        source: names
    });
    $("#search_form").submit(function(event){
        event.preventDefault()
        var search = $("#search").val();
        if (validation(search)){
            $("#warn").empty();
            $("#result").empty();
            window.location.href = "/search/" + search
        }
        else {
            $("#warn").empty();
            if (search.replace(/\s+/g, "").length == 0){
                let warning = $("<div></div>");
                warning.html("Input cannot be all whitespaces");
                $("#warn").append(warning);
                $("#search").focus();
                $("#search").val("");
            }
        }

    });

    $("#search").keypress(function(event){
        if(event.keyCode === 13) {
            event.preventDefault();
            $("#search_form").submit();
        }
    })
});