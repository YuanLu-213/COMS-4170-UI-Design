function display_data(index, item){
    var popular= $("<div class='col-md-4'></div>")
    var block = $("<div class='car'></div>")
    var image_link = $("<a href='/view/" + item["id"] + "'></a>")
    let res_img = $("<img class='car_img' src='" + item["image"] + "' alt='photo of " + item["name"] + "'>");
    image_link.html(res_img);

    block.append(image_link);

    var block_info = $("<div class='car-info'></div>");
    let res_name = $("<div id='cartitle'></div>");
    res_name.html(item["name"]);
    block_info.append(res_name);

    var type = $("<div id='type'></div>");
    type.html(item['type']);
    block_info.append(type);

    var text = $("<div id='des'></div>")
    var des = $("<p id='text'></p>");
    des.html(item['description']);
    text.append(des)
    block_info.append(text);
    block.append(block_info);

    popular.append(block);
    return popular
}

$(document).ready(function(){
    $("#input").autocomplete({
        source: names
    });

    $.each(data, function(index, item){

        var car = display_data(index, item)

        $(".row1").append(car);
    });
});