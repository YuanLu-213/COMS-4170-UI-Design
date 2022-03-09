$(document).ready(function(){
    var name = item["name"];
    var image_link = $("<a class='link' href='" + item["highlight"] + "'><>");
    var view_img = ("<img class='view_img rounded mx-auto d-block img-thumbnail' src='" + item["image"] + "' alt='photo of " + item["name"] + "'>");
    image_link.html(view_img);
    $("#image").append(image_link);

    var price = item["price"].toFixed(2).replace(/\d(?=(\d{3})+\.)/g, "$&,");
    $("#title").html(name);
    $("#price").children().append("$" + price);
    $("#door").children().append(item["doors"]);

    $("#description").append(item["description"]);
    $("#drive").append(item["spec"][0]["drive"]);
    $("#engine").append(item["spec"][0]["engine"]);
    $("#transmission").append(item["spec"][0]["transmission"]);
    $("#fuel").append(item["spec"][0]["fuel"]);

    $("#tab-2").hide();
    $("#tabs li:first").attr("id","current");
    $("tab-1").fadeIn(); 
    $("#tabs ul li:first").addClass("selected");
    $('#tabs li a').click(function(e) {
        e.preventDefault();
        $("#tabs ul li").removeClass("selected");
        $(e.currentTarget).parent("li").addClass("selected");
        if ($(this).attr("id") == "current"){
        return       
        }
        else{             
        $(".ui-tabs-panel").hide();
        $("#tabs li").attr("id","");
        $(this).parent().attr("id","current"); 

        $( $(this).attr('href')).fadeIn(); 
        }
    });

    $("#edit").click(function(){
        window.location.href = "/edit/" + id;
    })
})