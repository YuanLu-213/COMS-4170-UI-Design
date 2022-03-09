from crypt import methods
from flask import Flask
from flask import render_template, request, jsonify, Response, redirect
import random
app = Flask(__name__)

data = [
    {
        "id": 1,
        "name": "Rolls Royce Phantom",
        "type": "Sedan",
        "image": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2022-rolls-royce-phantom-mmp-1-1634759496.jpg",
        "highlight": "https://www.youtube.com/watch?v=BjqPGa7f6aw&t=529s",
        "description": "It's about the size of a tiny house and 10 times as expensive, but the 2022 Rolls-Royce Phantom justifies its price tag with the most luxurious cabin in autodom and the exclusivity that's built into a half-million-dollar car. The outside may cast a familiar decades-old silhouette, but the Phantom's interior is packed with modern conveniences and high-tech features to accompany its truly sumptuous environs. A V-12 engine provides seemingly endless power, yet it purrs silently under the Phantom's long hood so as not to disturb the interior's restful ambience. Fine leathers, real wood, and genuine metal parts cover every square inch of the cabin, and those relegated to the rear seat can relax in utmost comfort, especially in the long-wheelbase Extended model.",
        "price": 450000,
        "doors": 4,
        "spec": [
            {
                "drive": "All Wheel Drive",
                "engine": "Twin-Turbocharged and Intercooled DOHC 48-valve V-12",
                "transmission": "8-speed Automatic",
                "fuel":"Gasoline",
            }
        ]
    },
    {
        "id": 2,
        "name": "Lamborghini Urus",
        "type": "SUV",
        "image":"https://seriesmotor.com/wp-content/uploads/2022/01/Lamborghini-celebrates-best-ever-year-four-new-models-in-2022.jpg",
        "highlight": "https://www.youtube.com/watch?v=66_OVCQj-eM",
        "description": "While rival Ferrari is slow introducing its own exotic SUV, the Urus is pretty much alone in its class. Returning with no changes for 2022, this Italian bull might use the same platform as the Audi Q7 and Porsche Cayenne, but it stands out with a twin-turbocharged 4.0-litre V8 engine that unleashes 641 horsepower and accelerates from 0-100 km/h in just 3.6 seconds. A hybrid variant due by 2024 will raise the bar for performance.",
        "price": 256986,
        "doors": 4,
        "spec": [
            {
                "drive": "All Wheel Drive",
                "engine": "Twin-Turbocharged and Intercooled DOHC 32-valve V-8",
                "transmission": "8-speed Automatic",
                "fuel": "Gasoline",
            }
        ]

    },
    {
        "id": 3,
        "name": "Rolls Royce Cullinan",
        "type": "SUV",
        "image": "https://i.gaw.to/vehicles/photos/40/28/402815-2022-rolls-royce-cullinan.jpg",
        "highlight": "https://www.youtube.com/watch?v=G8_6p08DpCk&list=RDCMUCPOhQupz3MwGSIBG0OqVnAg&index=1",
        "description": "As one would expect of an ultra-expensive SUV, the 2022 Rolls-Royce Cullinan rides with supreme serenity and indulges everyone aboard. A strong and silky V-12 effortlessly motivates this quarter-million-dollar people mover. Though its exterior design borders on awkward, its unmistakable hood ornament and prodigious proportions ensure that onlookers know it’s a Rolls-Royce—and that its occupants are extremely wealthy. We only wish the interior wasn't marred by modern trends such as digital gauges, and we’d prefer that the standard back seat was more adjustable. Still, the quietness and build quality of the Cullinan's cabin is unrivaled, as is the ability to personalize the space to the owner's desire.",
        "price": 410575,
        "doors": 4,
        "spec": [
            {
                "drive": "All Wheel Drive",
                "engine": "Twin-Turbocharged and Intercooled DOHC 48-valve V-12",
                "transmission": "8-speed Automatic",
                "fuel": "Gasoline",
            }
        ]

    },
    {
        "id": 4,
        "name": "Mercedes Maybach GLS-600",
        "type": "SUV",
        "image": "https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/gallery_slide/public/images/car-reviews/first-drives/legacy/1-mercedes-maybach-gls600-2020-first-drive-review-hero-front.jpg?itok=Kdh0AYHf",
        "highlight": "https://www.youtube.com/watch?v=oUp2iMyXBSA&list=RDCMUCPOhQupz3MwGSIBG0OqVnAg&index=2",
        "description": "Vehicles wearing the Maybach badge, such as the 2022 Mercedes-Maybach GLS600, offer the utmost in luxury and deliver a transportation experience as rich as caviar. A twin-turbocharged V-8 is under the hood and drives all four wheels through a standard nine-speed automatic. Power is plentiful and the GLS600 glides along with on air suspension. But the GLS600 is less about its powertrain and chassis and more about its overstuffed cabin, which is fit for the real kings, sports stars, and hedge-fund managers who will own one of these posh palaces-on-wheels. Nappa leather, premium wood, and other high-end finishes give the interior a lounge-like environment. A pair of rear seats recline and massage you. The trade-off is that the GLS600 isn't as practical as its Benz- and AMG-branded counterparts, as it is not offered with a third row of seats and its cargo area is far less capacious. That will not be a problem for those buyers who seek out its sybaritic qualities",
        "price":161550,
        "doors":4,
        "spec": [
            {
                "drive": "All Wheel Drive",
                "engine": "Twin-Turbocharged and Intercooled DOHC 32-valve V-8",
                "transmission": "9-speed Automatic",
                "fuel": "Gasoline",
            }
        ]

    },
    {
        "id": 5,
        "name": "Bentley Continental GT",
        "type": "Sports Sedan",
        "image": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2022-bentley-continental-gt-speed-128-1620193617.jpg?crop=0.675xw:0.493xh;0.162xw,0.257xh&resize=1200:*",
        "highlight": "https://www.youtube.com/watch?v=Sypl-XF97O0",
        "description":"Although it's designed to make you feel like you've arrived, the 2022 Bentley Continental GT is also great car at making the journey memorable. The GT stands for grand touring, and the Conti's cabin is truly grand, pampering its occupants with fine leather, gorgeous wood, and handsome metal trims mixed with modern technology, plentiful amenities and enough cargo space for those who wouldn't deign to pack light. Both a coupe and a convertible are offered, as is a high-performance Speed variant. The Continental GT boasts a well-balanced chassis with just the right amount of athleticism for twisty canyon roads along with a smooth ride. All of this greatness comes at a steep price, but the six-figure outlay only serves to enhance the Bentley Continental GT's curb appeal.",
        "price": 277625,
        "doors": 2,
        "spec": [
            {
                "drive": "All Wheel Drive",
                "engine": "Twin-Turbocharged and Intercooled DOHC 48-valve W-12",
                "transmission": "8-speed Dual-clutch Automatic",
                "fuel": "Gasoline",
            }
        ]

    },
    {
        "id": 6,
        "name": "Ferrari SF90 Stradale",
        "type": "Sports Sedan",
        "image":"https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2021-ferrari-sf90-stradale-102-1626707777.jpg?crop=0.572xw:0.643xh;0.309xw,0.134xh&resize=640:*",
        "highlight": "https://www.youtube.com/watch?v=oeZVfWLKtqQ&list=RDCMUCPOhQupz3MwGSIBG0OqVnAg&index=1",
        "description": "Italian sports car icon Ferrari isn't the first brand that comes to mind when thinking about plug-in hybrid powertrains, but the 2022 SF90 Stradale and Spider models offer an electrified setup with 986 horsepower. When we tested one at Indianapolis Motor Speedway, we recorded a zero-to-60-mph time of just 2.0 seconds, which makes it officially the quickest car to 60 mph that we've ever tested. Let's see your Hyundai Ioniq or Toyota Prius Prime plug-ins do that. Not only does the SF90 deliver blistering acceleration and otherworldly handling, it also offers a fairly luxurious cabin lined with fine leather and decked out plenty of creature comforts. If you are one of the lucky few who can afford its half-million-dollar price tag, you'll find this Ferrari is worth it.",
        "price": 511250,
        "doors": 2,
        "spec": [
           {
                "drive": "All Wheel Drive",
                "engine": "Twin-Turbocharged and Intercooled DOHC 32-valve 4.0-liter V-8",
                "transmission": "8-speed Dual-clutch Automatic",
                "fuel": "Gasoline",
            }   
        ]

    },
    {
        "id": 7,
        "name": "Lamborghini Huracán Evo",
        "type": "Sports Sedan",
        "image": "https://imageio.forbes.com/specials-images/imageserve/6170980fde149f460fd08f30/0x0.jpg?format=jpg&width=1200&fit=bounds",
        "highlight": "https://www.youtube.com/watch?v=fKNdoxRld34",
        "description": "The 2022 Lamborghini Huracán draws everyone's attention, but it's the way it assaults the driver's senses that makes it special. The main attraction is the 600-plus-hp naturally aspirated V-10 that mounted in the middle of the exotic-looking Lamborghini. The engine sounds magnificent when revved to its lofty redline, and it helps deliver hilariously quick acceleration. The Huracán can be configured as a coupe or as the Spyder convertible, and both offer rear- or all-wheel drive. While the only way to truly unlock the full potential of its incredible performance is to go to a racetrack, it's ride is surprisingly civil when driven on public roads. Just don't expect the Lambo to be a great travel companion due to its limited interior cubby storage. Otherwise, the 2022 Huracán has all the hallmarks of supercar stardom—including a six-figure price tag.",
        "price": 453396,
        "doors": 2,
        "spec": [
           {
                "drive": "Rear Wheel Drive",
                "engine": "DOHC 40-valve V-10",
                "transmission": "7-speed Dual-clutch Automatic",
                "fuel": "Gasoline",
            }   
        ]

    },
    {
        "id": 8,
        "name": "McLaren 720S",
        "type": "Sports Sedan",
        "image": "https://i.gaw.to/vehicles/photos/40/28/402886-2022-mclaren-720s.jpg?1024x640",
        "highlight": "https://www.youtube.com/watch?v=eLJ6nW8bfTw",
        "description": "Like many exotic cars, the 2022 McLaren 720S offers a lot of show and serious go. The thrills include explosive launches and the kind of ethereal agility that'll send serious drivers into ecstasy. At the heart of McLaren's lightweight, carbon-fiber-intensive dream machine is a 710-hp twin-turbo V-8. While the engine has considerable turbo lag, the short pause after you stomp the accelerator allows a beat to prepare for a rush to 100 mph in just 5.2 seconds and the ability to reach a claimed 212 mph. When 720S coupe or Spider (read: convertible) drivers aren't living out their Formula 1 fantasies, they’ll find the car provides a surprisingly civil ride. The only real pain is the contortions required to climb out of its simple yet customizable interior. Yes, the 2022 720S is insanely pricey, but that money buys a car that's insanely special.",
        "price":411300,
        "doors":2,
        "spec": [
           {
                "drive": "Rear Wheel Drive",
                "engine": "Twin-Turbocharged and Intercooled DOHC 32-valve V-8",
                "transmission": "7-speed Dual-clutch Automatic",
                "fuel": "Gasoline",
            }   
        ]

    },
    {
        "id": 9,
        "name": "Aston Martin Vantage",
        "type": "Sports Sedan",
        "image":"https://blog.dupontregistry.com/wp-content/uploads/2021/11/astonmartinvantagef1-1.jpg",
        "highlight": "https://www.youtube.com/watch?v=8LYgIGQzTaQ",
        "description": "A sports car's primary mission is to make the driver feel behind the wheel, and the beautiful 2022 Aston Martin Vantage does all that while making heads turn everywhere it goes. Its sensual shape­–available with a fixed roof or a retractable soft top­–is classic sport's car stuff, with a long hood and wide haunches. What's under that clamshell hood is almost equally as lusty: a 500-plus-hp twin-turbo V-8 sourced from Mercedes-AMG. This vociferous mill mates with a manual or automatic transmission, but unfortunately the former is only offered on the regular coupe. For driver's looking to channel their inner Sebastian Vettel, Aston now offers a track-tuned F1 Edition with distinct styling, an enhanced chassis, and extra horsepower. While the Vantage's interior suffers from some fit-and-finish issues and uncouth wind and road noise at highway speeds, the highly customizable cabin can still be lavishly appointed. Most importantly, Aston Martin's entry-level machine constantly manufactures smiles and stares.",
        "price": 150086,
        "doors": 2,
        "spec": [
           {
                "drive": "Rear Wheel Drive",
                "engine": "Twin-Turbocharged and Intercooled DOHC 32-valve V-8",
                "transmission": "8-speed Automatic",
                "fuel": "Gasoline",
            }   
        ]

    },
    {
        "id": 10,
        "name": "Mercedes-Benz AMG G-63",
        "type": "SUV",
        "image": "https://images2.alphacoders.com/105/thumb-1920-1058423.jpg",
        "highlight": "https://www.youtube.com/watch?v=eErTb3cKqcI",
        "description": "Mercedes-Benz's iconic G-wagen SUV has roots as a military vehicle, but the high-performance 2022 Mercedes-AMG G63 model serves an entirely different driver than the 1970s original. A 577-hp twin-turbocharged V-8 engine gives the G63 incredible performance, and its posh cabin offers all the modern amenities we've come to expect from a top-spec Mercedes. A host of infotainment and other tech features that would have seemed like science fiction to the designers of the original truck are standard. Want to go off road? The G63 can tackle those tasks too, although we'd be nervous about nicking its sporty-looking 20-inch wheels. No matter how you intend to use it, though, the G63 is built to impress—and its price tag reflects both its skillset and status",
        "price": 175945,
        "doors": 4,
        "spec": [
            {
                "drive": "All Wheel Drive",
                "engine": "Twin-Turbocharged and Intercooled DOHC 32-valve V-8",
                "transmission": "9-speed Automatic",
                "fuel": "Gasoline",
            }
        ]

    },
    {
        "id": 11,
        "name": "Bugatti Chiron",
        "type": "Sports Sedan",
        "image": "https://www.gtopcars.com/wp-content/uploads/2021/07/2022-Bugatti-Chiron-SS.jpg",
        "highlight": "https://youtu.be/NJDU5p6iU2k",
        "description": "The 2022 Chiron isn't only the ultimate Bugatti, it's the ultimate car. Period. This $3 million work of art is capable of pummeling the pavement at over 200 mph thanks to a 16-cylinder engine that features four turbochargers and cranks out at least 1500 horsepower—the more expensive Super Sport model is even more powerful. The Chiron's cabin is just as artfully designed as its exterior, and it coddles occupants in fine materials that help justify its price tag. But let's be honest, people are really paying for the performance here. Those looking for modern conveniences (think Apple CarPlay) or driver-assistance tech, they won't find them here, but after driving this monster, they likely won't care about such minor drawbacks.",
        "price": 3900000,
        "doors": 2,
        "spec": [
            {
                "drive": "All Wheel Drive",
                "engine": "Quad-Turbocharged Intercooled DOHC 64-valve W-16",
                "transmission": "7-speed Dual-clutch Automatic",
                "fuel": "Gasoline",
            }
        ]

    },
    {
        "id": 12,
        "name": "Land Rover Range Rover",
        "type": "SUV",
        "image": "https://hips.hearstapps.com/hmg-prod/images/2020-land-rover-range-rover-mmp-1-1573162813.jpg?crop=0.670xw:0.750xh;0.143xw,0.250xh&resize=640:*",
        "highlight": "https://youtu.be/Y-6nZhJk8ps",
        "description": "Although it has blue-collar roots dating back more than a half-century the 2022 Range Rover's high-end interior and first-class curb appeal are designed to attract wealthy, white-collar buyers. While its transformation has been decades in the making, this leather-lined limo has reached a point where it's nearly six-figure starting price seems an appropriate ask. The cabin features upscale finishes such as leather, wood, and thickly-piled carpeting. And there’s plenty of tech too. Buyers can choose either a turbocharged inline-six or a thundering 523-hp twin-turbo V-8 engine, but all models come standard with off-road-capable features, such as an all-wheel-drive system, a rear-wheel steering system, and an air suspension that can be raised for extra ground clearance. Few Range Rover owners would dare to venture too far from paved roads, but knowing you could if you wanted to is, in fact, a luxury. In an odd twist, this new generation of Range Rover, launched for the 2022 model year will sell alongside a 2022 model of the previous generation until inventory runs out.",
        "price": 159550,
        "doors": 4,
        "spec": [
            {
                "drive": "All Wheel Drive",
                "engine": "Twin-Turbo 4.4-liter V-8",
                "transmission": "8-speed Automatic",
                "fuel": "Gasoline",
            }
        ]

    }
]

@app.route("/")
def home_page():

    names = []
    for item in data:
        names.append(item["name"])

    return render_template('home.html', names=names, data=data)


@app.route("/search/<keys>", methods=["GET", "POST"])
def search(keys):
    global data

    names = []
    keyword = keys

    for item in data:
        names.append(item["name"])

    result = []

    for item in data:
        if keys.lower() in item["name"].lower():
            items = item
            items["match"] = "name"
            items["start"] = item["name"].lower().find(keys.lower())
            items["end"] = items["start"] + len(keys)
            result.append(items)
        elif keys.lower() in item["type"].lower():
            items = item
            items["match"] = "type"
            items["start"] = item["type"].lower().find(keys.lower())
            items["end"] = items["start"] + len(keys)
            result.append(items)
        elif keys.lower() in item["spec"][0]["drive"].lower():
            items = item
            items["match"] = "drive"
            items["start"] = item["spec"][0]["drive"].lower().find(keys.lower())
            items["end"] = items["start"] + len(keys)
            result.append(items)
    
    return render_template('search.html', results=result, names=names, keyword=keyword)

@app.route("/view/<id>")
def view(id):
    global data

    names = []
    for item in data:
        names.append(item["name"])

    for item in data:
        if int(id) == item["id"]:
            return render_template("view.html", item=item, names=names, id=id)
        else:
            print("id not valid")

@app.route("/add")
def add():

    names = []
    for item in data:
        names.append(item["name"])

    return render_template("add.html", names=names)

@app.route("/add_car", methods=["GET", "POST"])
def add_car():
    global data
    
    current_id = data[-1]["id"]

    added_car = request.get_json()
    added_car["id"] = current_id + 1
    print(added_car)
    data.append(added_car)

    return jsonify(url="view/" + str(added_car["id"]))


@app.route("/edit/<id>")
def edit(id):
    global data

    for item in data:
        if int(id) == item["id"]:
            return render_template("edit.html", item=item)
        else:
            print("id not valid")

@app.route("/edit_car", methods=["GET","POST"])
def edit_car():
    global data

    edited_car = request.get_json()
    for item in data:
        if edited_car["name"] == item["name"]:
            if edited_car["image"] != item["image"]:
                item["image"] = edited_car["image"]
            if edited_car["highlight"] != item["highlight"]:
                item["highlight"] = edited_car["highlight"]
            if edited_car["description"] != item["description"]:
                item["description"] = edited_car["description"]
            if edited_car["price"] != item["price"]:
                item["price"] = edited_car["price"]
            if edited_car["doors"] != item["doors"]:
                item["doors"] = edited_car["doors"]
            if edited_car["spec"][0]["drive"] != item["spec"][0]["drive"] :
                item["spec"][0]["drive"]  = edited_car["spec"][0]["drive"] 
            if edited_car["spec"][0]["engine"] != item["spec"][0]["engine"] :
                item["spec"][0]["engine"]  = edited_car["spec"][0]["engine"] 
            if edited_car["spec"][0]["transmission"] != item["spec"][0]["transmission"] :
                item["spec"][0]["transmission"]  = edited_car["spec"][0]["transmission"] 
            if edited_car["spec"][0]["fuel"] != item["spec"][0]["fuel"] :
                item["spec"][0]["fuel"]  = edited_car["spec"][0]["fuel"] 

    print(data)
    return jsonify(0)


