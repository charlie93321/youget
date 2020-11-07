import os
import traceback
from _csv import reader

import xlrd
from xlrd import XLRDError

from com.dxm.lazadaAttr.script.excel_util import write_date_to_xls, write_data_to_xls

dicMap = {}
dicCount = []
#dir1 = r'C:\Users\DXM_0093\Desktop\lazada分类_zxy'
dir1 = r'C:\Users\DXM_0093\Desktop\lazada分类_ljl'
#dir1 = r'C:\Users\DXM_0093\Desktop\Lazada分类树（印尼语）'
file_names = os.listdir(dir1)[:2]
# file_names=sorted(file_names,key=lambda x:int(x.split(".")[0]))




def read_excel():
    with open('record.txt',mode='w',encoding='utf-8') as f:
        for file_name in file_names:
            path = "{}/{}".format(dir1, file_name)
            if file_name.endswith(".csv") or file_name == 'Lazada分类-越南语.xlsx':
                print("{} is not xls".format(path))
                continue

            sheet = None
            x1 = None
            try:
                x1 = xlrd.open_workbook(path)
                sheet = x1.sheet_by_name('Upload Template')
            except XLRDError as e:
                print("{} can't get sheet {}".format(path, 'Upload Template'))
                print('str(e):\t\t', str(e))
                print('repr(e):\t', repr(e))
                print('traceback.print_exc():')
                # 以下两步都是输出错误的具体位置的
                traceback.print_exc()
                #print('traceback.format_exc():\n%s' % traceback.format_exc())
                continue
            finally:
                x1.release_resources()
            #print("{}  get sheet ===> sheets=>{}".format(path, x1.sheet_names()))

            row1 = sheet.row(1)
            row2 = sheet.row(2)
            for i in range(1, len(row1)):
                key = row2[i].value.strip()
                value = row1[i].value.replace('*', '').strip()
                dicMap[(key,file_name)] = value
                print(key,value,file_name)
                f.write('key:{},value:{},file_name:{}'.format(key,value,file_name))
            dicCount.append(i)

            x1.release_resources()


#write_date_to_xls(file_name='lazada_th_attr.xls',dataMap=dicMap,title=['EN','TH'])
# write_date_to_xls(file_name='lazada_vi_attr.xls',dataMap=dicMap,title=['EN','VI'])
#write_date_to_xls(file_name='lazada_id_attr.xls', dataMap=dicMap, title=['EN', 'ID'])

read_excel()

lines='''
站点	属性标记	越南语
VN	Style	Style
VN	2 in 1 Type	2 in 1 Type_translate
VN	3D Glasses Type	3D Glasses Type_translate
VN	AC Adapter	AC Adapter_translate
VN	ADF Capacity	ADF Capacity_translate
VN	ADF tray	ADF tray_translate
VN	About Product	About Product_translate
VN	About The Brand	About The Brand_translate
VN	About The Store	About The Store_translate
VN	Accessories	Accessories_translate
VN	Accessories Style	Accessories Style_translate
VN	Accessory Type	Accessory Type_translate
VN	Activity	Activity_translate
VN	Activity Type	Activity Type_translate
VN	Additives	Additives_translate
VN	Adhesive Product Type	Adhesive Product Type_translate
VN	Adjustible	Adjustible_translate
VN	Age Group	Age Group_translate
VN	Age Restriction	Age Restriction_translate
VN	Age Suitablilty	Age Suitablilty
VN	Age range suitability	Age range suitability
VN	Age_suitability (Weight)	Age_suitability (Weight)
VN	Air Conditioner Features	Air Conditioner Features
VN	Air Conditioner Rated Capacity (BTUs)	Air Conditioner Rated Capacity (BTUs)
VN	Air Conditioner Rated Capacity (HP)	Air Conditioner Rated Capacity (HP)
VN	Air Conditioning type	Air Conditioning type
VN	Air Cooler Features	Air Cooler Features
VN	Air Fryer Features	Air Fryer Features
VN	Air Humidifier Features	Air Humidifier Features
VN	Air Humidifier Parts Type	Air Humidifier Parts Type
VN	Air Purifier Features	Air Purifier Features
VN	Air Purifier Filtration Type	Air Purifier Filtration Type
VN	Alcohol Percentage (%)	Alcohol Percentage (%)
VN	Amperage (amp)	Amperage (amp)
VN	Animal Type	Animal Type
VN	Antenna Type	Antenna Type
VN	Antennas	Antennas
VN	Anti Slip	Anti Slip
VN	Anti-colic	Anti-colic
VN	Antitheft type	Antitheft type
VN	Applicable Area	Applicable Area
VN	Application	Application
VN	Arrangement	Arrangement
VN	Artist	Artist
VN	Artist name	Artist name
VN	Aspect Ratio	Aspect Ratio
VN	Assembly	Assembly
VN	Audio Output Mode	Audio Output Mode
VN	Author	Author
VN	Auto Battery Size	Auto Battery Size
VN	Auto Focus Points	Auto Focus Points
VN	Auto Shut Off	Auto Shut Off
VN	Available Location by Postal Code	Available Location by Postal Code
VN	Axle Type	Axle Type
VN	BBQ Fuel Type	BBQ Fuel Type
VN	BBQ Shape	BBQ Shape
VN	BTU Rating	BTU Rating
VN	Baby Clothing Size	Baby Clothing Size
VN	Baby Flavor	Baby Flavor
VN	Baby Material	Baby Material
VN	Baby Organic	Baby Organic
VN	Baby Recommended Age	Baby Recommended Age
VN	Baby Scent	Baby Scent
VN	Baby Skin Type	Baby Skin Type
VN	Baby Weight	Baby Weight
VN	Backpack Capacity (liters)	Backpack Capacity (liters)
VN	Bag Dimension	Bag Dimension
VN	Bag Shape	Bag Shape
VN	Bag Type	Bag Type
VN	Bakeware Material	Bakeware Material
VN	Baking Dish Type	Baking Dish Type
VN	Baking Tray Type	Baking Tray Type
VN	Baking Utensil Type	Baking Utensil Type
VN	Ball Size (cm)	Ball Size (cm)
VN	Ball type	Ball type
VN	Barware Type	Barware Type
VN	Bathrobe Size	Bathrobe Size
VN	Bathroom Fitting Type	Bathroom Fitting Type
VN	Bathroom Tapware Type	Bathroom Tapware Type
VN	Batteries	Batteries
VN	Batteries Type	Batteries Type
VN	Battery Accessories Type	Battery Accessories Type
VN	Battery Average Life	Battery Average Life
VN	Battery Capacity	Battery Capacity
VN	Battery Core Type	Battery Core Type
VN	Battery Features	Battery Features
VN	Battery Life Run Time (Min)	Battery Life Run Time (Min)
VN	Battery Size	Battery Size
VN	Battery Type	Battery Type
VN	Battery Voltage	Battery Voltage
VN	Battery_Life_(Min)	Battery_Life_(Min)
VN	Battery_Type	Battery_Type
VN	Beach Style	Beach Style
VN	Bearing number	Bearing number
VN	Bed Accessory Type	Bed Accessory Type
VN	Bed Sheet Type	Bed Sheet Type
VN	Bed Type	Bed Type
VN	Bedding Size	Bedding Size
VN	Bedding_Pattern	Bedding_Pattern
VN	Beer Style	Beer Style
VN	Belt Material	Belt Material
VN	Belt Styles	Belt Styles
VN	Benefits	Benefits
VN	Bike Frame Size (inches)	Bike Frame Size (inches)
VN	Bike_Frame_Material	Bike_Frame_Material
VN	Bike_Frame_Size_(cm)	Bike_Frame_Size_(cm)
VN	Bike_Wheel_Size_(Dia/inch)	Bike_Wheel_Size_(Dia/inch)
VN	Bin Type	Bin Type
VN	Binder Edge Type	Binder Edge Type
VN	Binder Type	Binder Type
VN	Blade Side (inches)	Blade Side (inches)
VN	Blanket Length	Blanket Length
VN	Blanket Width	Blanket Width
VN	Blender Features	Blender Features
VN	Blouse Sleeve Style	Blouse Sleeve Style
VN	BluRay 3D Features	BluRay 3D Features
VN	Bluetooth	Bluetooth
VN	Bluray Features	Bluray Features
VN	Board Type	Board Type
VN	Body Armor type	Body Armor type
VN	Body Care Benefits	Body Care Benefits
VN	Body Material	Body Material
VN	Body Only	Body Only
VN	Body Scrub Formulation	Body Scrub Formulation
VN	Body jewellery	Body jewellery
VN	Book_Format	Book_Format
VN	Bookcase design	Bookcase design
VN	Boot Height	Boot Height
VN	Boot Type	Boot Type
VN	Bottle Stage	Bottle Stage
VN	Bottle Type	Bottle Type
VN	Bottle compatibility	Bottle compatibility
VN	Bottle pack size	Bottle pack size
VN	Bottom Type	Bottom Type
VN	Bowl Material	Bowl Material
VN	Bra Type	Bra Type
VN	Bracelet Size	Bracelet Size
VN	Brake & Repair Tools type	Brake & Repair Tools type
VN	Brake Fluid Type	Brake Fluid Type
VN	Brand	Brand
VN	Brand Classification	Brand Classification
VN	Brand Compatibility	Brand Compatibility
VN	Breastpump compatibility	Breastpump compatibility
VN	Bridge System	Bridge System
VN	Broom Type	Broom Type
VN	Brush Type	Brush Type
VN	Buildin Oven Heating Methods	Buildin Oven Heating Methods
VN	Built in Microphone	Built in Microphone
VN	Built-in Battery	Built-in Battery
VN	Built-in Oven Features	Built-in Oven Features
VN	Bulb Cap Type	Bulb Cap Type
VN	Bulb Socket Type	Bulb Socket Type
VN	Bulb Type	Bulb Type
VN	Bundesliga Teams	Bundesliga Teams
VN	Bundle	Bundle
VN	Burner Type	Burner Type
VN	Bus Type	Bus Type
VN	CB Radios & Scanners type	CB Radios & Scanners type
VN	CPU Chipset Model	CPU Chipset Model
VN	CPU Number cooling Type	CPU Number cooling Type
VN	Cabin Size Compatibility	Cabin Size Compatibility
VN	Cable Length (M)	Cable Length (M)
VN	Cable Type	Cable Type
VN	Cake Pan Shape	Cake Pan Shape
VN	Cake Pan Type	Cake Pan Type
VN	Calculator Power Source	Calculator Power Source
VN	Calculator Type	Calculator Type
VN	Camera Additional Accessories	Camera Additional Accessories
VN	Camera Brand Compatibility	Camera Brand Compatibility
VN	Camera Front	Camera Front
VN	Can Opener Type	Can Opener Type
VN	Capacity	Capacity
VN	Capacity (L)	Capacity (L)
VN	Capacity (Lit)	Capacity (Lit)
VN	Capacity (Liters)	Capacity (Liters)
VN	Capacity (no of People)	Capacity (no of People)
VN	Capacity Battery	Capacity Battery
VN	Capacity_(Lit)	Capacity_(Lit)
VN	Capacity_(l)	Capacity_(l)
VN	Car Make and Model	Car Make and Model
VN	Car Model	Car Model
VN	Car Polishes & Waxes type	Car Polishes & Waxes type
VN	Cargo Management type	Cargo Management type
VN	Carpet Type	Carpet Type
VN	Carrying Position	Carrying Position
VN	Carton	Carton
VN	Cartridge Printer Paper Type	Cartridge Printer Paper Type
VN	Case Theme	Case Theme
VN	Case Type	Case Type
VN	Case/Cover Function	Case/Cover Function
VN	Case/Cover Material	Case/Cover Material
VN	Cat Breed	Cat Breed
VN	Cat Life Stage	Cat Life Stage
VN	Caulking Category	Caulking Category
VN	Caulking Type	Caulking Type
VN	Ceiling Fan Features	Ceiling Fan Features
VN	Cellular	Cellular
VN	Cereal Type	Cereal Type
VN	Certifications Endorsements	Certifications Endorsements
VN	Chain Size	Chain Size
VN	Chair Arms	Chair Arms
VN	Chair Back Height	Chair Back Height
VN	Chair Back Panel Style	Chair Back Panel Style
VN	Chair Design	Chair Design
VN	Chair Type	Chair Type
VN	Channel Quantity	Channel Quantity
VN	Character and Design	Character and Design
VN	Characters	Characters
VN	Cheese Tool Type	Cheese Tool Type
VN	Chest&Back Protectors Type	Chest&Back Protectors Type
VN	Chipset	Chipset
VN	Chipset Manufacturer	Chipset Manufacturer
VN	Chocolate Type	Chocolate Type
VN	City	City
VN	Clip Type	Clip Type
VN	Clock Type	Clock Type
VN	Clothing Decoration	Clothing Decoration
VN	Clothing Material	Clothing Material
VN	Cloths & Towels type	Cloths & Towels type
VN	Clutches & Parts type	Clutches & Parts type
VN	Coasters	Coasters
VN	Coffee Accessory Type	Coffee Accessory Type
VN	Coffee Machine Features	Coffee Machine Features
VN	Coffee Machine Type	Coffee Machine Type
VN	Coffee Maker Type	Coffee Maker Type
VN	Coffee/Tea Server Type	Coffee/Tea Server Type
VN	Collar Style / Neckline	Collar Style / Neckline
VN	Collar Type	Collar Type
VN	Collar Type/ Neckline	Collar Type/ Neckline
VN	Collar Type/Neckline	Collar Type/Neckline
VN	Color	Color
VN	Color Family	Color Family
VN	Color Group	Color Group
VN	Color thumbnail	Color thumbnail
VN	Coloured gems type	Coloured gems type
VN	Compatibility	Compatibility
VN	Compatibility by Model	Compatibility by Model
VN	Compatible Car Model	Compatible Car Model
VN	Compatible Devices	Compatible Devices
VN	Compatible Laptop Size	Compatible Laptop Size
VN	Compatible Media	Compatible Media
VN	Compatible Motorcycle Brand	Compatible Motorcycle Brand
VN	Compatible Motorcycle Model	Compatible Motorcycle Model
VN	Compatible Operating System	Compatible Operating System
VN	Compatible Products	Compatible Products
VN	Computer Memory Type	Computer Memory Type
VN	Condition	Condition
VN	Connection	Connection
VN	Connectivity	Connectivity
VN	Connectivity Speed	Connectivity Speed
VN	Connectivity Type	Connectivity Type
VN	Console Model	Console Model
VN	Console Model Compatibility	Console Model Compatibility
VN	Console Type	Console Type
VN	Consoles & Organizers type	Consoles & Organizers type
VN	Cooking Preparation	Cooking Preparation
VN	Cooking Style	Cooking Style
VN	Cooking Utensil Type	Cooking Utensil Type
VN	Cooktop Ranges Features	Cooktop Ranges Features
VN	Cooktop Surface	Cooktop Surface
VN	Cooktop Type	Cooktop Type
VN	Cookware Capacity	Cookware Capacity
VN	Cookware Diameter (cm)	Cookware Diameter (cm)
VN	Cookware Features	Cookware Features
VN	Cookware Finish	Cookware Finish
VN	Cookware Length (cm)	Cookware Length (cm)
VN	Cookware Shape	Cookware Shape
VN	Cookware material	Cookware material
VN	Cooling System Type	Cooling System Type
VN	Cordless	Cordless
VN	Core Construction	Core Construction
VN	Correction Type	Correction Type
VN	Costume Theme	Costume Theme
VN	Count (pieces)	Count (pieces)
VN	Country of Origin	Country of Origin
VN	Cover Material	Cover Material
VN	Cover Type	Cover Type
VN	Create Year	Create Year
VN	Cuisine	Cuisine
VN	Cup Size	Cup Size
VN	Cup Type	Cup Type
VN	Curl	Curl
VN	Curl_Diameter	Curl_Diameter
VN	Curtain Features	Curtain Features
VN	Curtain Length (cm)	Curtain Length (cm)
VN	Curtain Length (mm)	Curtain Length (mm)
VN	Curtain Material	Curtain Material
VN	Curtain Type	Curtain Type
VN	Curtain Width (cm)	Curtain Width (cm)
VN	Cushion Type	Cushion Type
VN	Customer Support	Customer Support
VN	Cutlery Type	Cutlery Type
VN	Cutter Type	Cutter Type
VN	DDR Variant	DDR Variant
VN	Dangerous Goods	Dangerous Goods
VN	Data Rate	Data Rate
VN	Date of publishing	Date of publishing
VN	Days of Supply	Days of Supply
VN	De-humidifier Capacity (ml)	De-humidifier Capacity (ml)
VN	Decode Ability Type	Decode Ability Type
VN	Deflectors & Shields type	Deflectors & Shields type
VN	Delivery Option Economy	Delivery Option Economy
VN	Delivery Option Express	Delivery Option Express
VN	Delivery Option Instant	Delivery Option Instant
VN	Delivery Option Standard	Delivery Option Standard
VN	Delivery and handling	Delivery and handling
VN	Denim Features	Denim Features
VN	Denomination	Denomination
VN	Depth	Depth
VN	Design	Design
VN	Desk Chair Type	Desk Chair Type
VN	Desk Design	Desk Design
VN	Desk Features	Desk Features
VN	Desk Organizer Type	Desk Organizer Type
VN	Desk Shape	Desk Shape
VN	Device Compatibility	Device Compatibility
VN	Device Placement	Device Placement
VN	Dial Size (mm)	Dial Size (mm)
VN	Diamond Clarity	Diamond Clarity
VN	Diamond colour	Diamond colour
VN	Diamond cut	Diamond cut
VN	Diaper Pack Size	Diaper Pack Size
VN	Diaper Size	Diaper Size
VN	Diaper Type	Diaper Type
VN	Diary Type	Diary Type
VN	Dietary Information	Dietary Information
VN	Dietary Needs	Dietary Needs
VN	Dietary Requirements	Dietary Requirements
VN	Digital Zoom	Digital Zoom
VN	Dimension	Dimension
VN	Dimension of the door	Dimension of the door
VN	Dimensions	Dimensions
VN	Dining Table Type	Dining Table Type
VN	Dinner Plate Type	Dinner Plate Type
VN	Disc Size (inches)	Disc Size (inches)
VN	Dishwasher Type	Dishwasher Type
VN	Disk Type	Disk Type
VN	Display	Display
VN	Display Features	Display Features
VN	Display Size	Display Size
VN	Display Size (inches)	Display Size (inches)
VN	Dock Connector	Dock Connector
VN	Dock Features	Dock Features
VN	Dog Breed Type	Dog Breed Type
VN	Dog Life Stage	Dog Life Stage
VN	Dog Size	Dog Size
VN	Dog Weight	Dog Weight
VN	Door Hardware Type	Door Hardware Type
VN	Door Type	Door Type
VN	Double Sided Printing	Double Sided Printing
VN	Drawer Paper Size	Drawer Paper Size
VN	Dress Length	Dress Length
VN	Dress Style	Dress Style
VN	Dress Type	Dress Type
VN	Dresser Design	Dresser Design
VN	Drill Type	Drill Type
VN	Drip Stop	Drip Stop
VN	Drive Interface	Drive Interface
VN	Drone Features	Drone Features
VN	Dryer Type	Dryer Type
VN	Dryiing Rack Materials	Dryiing Rack Materials
VN	Drying Capacity	Drying Capacity
VN	Drying Capacity (kg)	Drying Capacity (kg)
VN	Drying Rack No. of Rails	Drying Rack No. of Rails
VN	Dumbell_Material	Dumbell_Material
VN	Dutch Oven Type	Dutch Oven Type
VN	E-Cigarette Type	E-Cigarette Type
VN	Earring Size	Earring Size
VN	Eco Credentials	Eco Credentials
VN	Edition	Edition
VN	Edition Type	Edition Type
VN	Electric Toothbrush Features	Electric Toothbrush Features
VN	Electric Toothbrush Type	Electric Toothbrush Type
VN	Electrical Tool Type	Electrical Tool Type
VN	End date of promotion	End date of promotion
VN	Energy Consumption (W)	Energy Consumption (W)
VN	Energy Efficiency (EGAT)	Energy Efficiency (EGAT)
VN	Energy Efficiency (No of stars)	Energy Efficiency (No of stars)
VN	Energy Efficiency Star	Energy Efficiency Star
VN	Energy efficiency (no of ticks	Energy efficiency (no of ticks
VN	Energy efficiency (no of ticks)	Energy efficiency (no of ticks)
VN	Energy_Consumption_Grade	Energy_Consumption_Grade
VN	Energy_Efficiency_Tick	Energy_Efficiency_Tick
VN	Engine Oil Type	Engine Oil Type
VN	Engine_oil_size	Engine_oil_size
VN	English Long Description (optional)	English Long Description (optional)
VN	Entertainment Type	Entertainment Type
VN	Envelope Type	Envelope Type
VN	Event	Event
VN	Expandable	Expandable
VN	Expandable Memory	Expandable Memory
VN	Exposure level for Film	Exposure level for Film
VN	External Storage	External Storage
VN	Extractor Type	Extractor Type
VN	Eyelash Volume	Eyelash Volume
VN	Eyes Makeup Finish	Eyes Makeup Finish
VN	Eyewear Shape	Eyewear Shape
VN	Eyewear size	Eyewear size
VN	Eyewear_Shape	Eyewear_Shape
VN	Fabric Feature	Fabric Feature
VN	Fabric Features	Fabric Features
VN	Fabrics	Fabrics
VN	Face Makeup Benefits	Face Makeup Benefits
VN	Face Makeup Coverage	Face Makeup Coverage
VN	Face Makeup Finish	Face Makeup Finish
VN	Fan Blade Materials	Fan Blade Materials
VN	Fan Dimensions	Fan Dimensions
VN	Fan Features	Fan Features
VN	Fan Speed	Fan Speed
VN	Fan Type	Fan Type
VN	Fastener Head Style	Fastener Head Style
VN	Fastener Length (mm)	Fastener Length (mm)
VN	Fastener Maximum Weight (kg)	Fastener Maximum Weight (kg)
VN	Fastener Surface Type	Fastener Surface Type
VN	Fastener Type	Fastener Type
VN	Fax color	Fax color
VN	Featured Characters Brand	Featured Characters Brand
VN	Features	Features
VN	File Size	File Size
VN	Filing Type	Filing Type
VN	Filling	Filling
VN	Film Size	Film Size
VN	Filter Diameter	Filter Diameter
VN	Filter Lifetime	Filter Lifetime
VN	Filter Type	Filter Type
VN	Finish	Finish
VN	Fire Alarm Power Type	Fire Alarm Power Type
VN	Fire Alarm Type	Fire Alarm Type
VN	Fire Blanket Features	Fire Blanket Features
VN	Fire Blanket Length (m)	Fire Blanket Length (m)
VN	Fire Extinguisher Class	Fire Extinguisher Class
VN	Fire Extinguisher Features	Fire Extinguisher Features
VN	Fire Extinguisher Medium	Fire Extinguisher Medium
VN	Fire Extinguisher Size (Kg)	Fire Extinguisher Size (Kg)
VN	Fire Ladder Length (m)	Fire Ladder Length (m)
VN	Fire Proof	Fire Proof
VN	Firmness of mattress	Firmness of mattress
VN	Fishing Rod Length (meter)	Fishing Rod Length (meter)
VN	Fishing Type	Fishing Type
VN	Fit Type	Fit Type
VN	Flag Type	Flag Type
VN	Flash Range (M)	Flash Range (M)
VN	Flavor	Flavor
VN	Flavor Nutrition	Flavor Nutrition
VN	Floaties Type	Floaties Type
VN	Floor Adhesive Type	Floor Adhesive Type
VN	Flour Type	Flour Type
VN	Flow Level	Flow Level
VN	Flushes	Flushes
VN	Focal Ratio	Focal Ratio
VN	Foldable	Foldable
VN	Folded Dimension	Folded Dimension
VN	Folded Length	Folded Length
VN	Food Feature	Food Feature
VN	Food Pairings	Food Pairings
VN	Foot Care Benefits	Foot Care Benefits
VN	Football Championships	Football Championships
VN	Football_Boot_Type	Football_Boot_Type
VN	Form Factor	Form Factor
VN	Form Gel	Form Gel
VN	Format	Format
VN	Format Magazines	Format Magazines
VN	Frame Color	Frame Color
VN	Frame Material	Frame Material
VN	Frame Rate	Frame Rate
VN	Frame colour	Frame colour
VN	Frame type	Frame type
VN	Free Gift	Free Gift
VN	Freezer Capacity	Freezer Capacity
VN	Freezer Type	Freezer Type
VN	Freshness	Freshness
VN	Freshness Metric	Freshness Metric
VN	Freshness_metric	Freshness_metric
VN	Fretboard Material	Fretboard Material
VN	Fruit Tool Type	Fruit Tool Type
VN	Fruit Type	Fruit Type
VN	Fulfillment Method	Fulfillment Method
VN	Function	Function
VN	Function Power	Function Power
VN	Furniture Features	Furniture Features
VN	GTIN	GTIN
VN	Game Genre	Game Genre
VN	Garlic Tool Type	Garlic Tool Type
VN	Garment Steamer Type	Garment Steamer Type
VN	Garment Type	Garment Type
VN	Gem Type	Gem Type
VN	Glassware Type	Glassware Type
VN	Glove Size	Glove Size
VN	Glue Type	Glue Type
VN	Graphic Card Chipset	Graphic Card Chipset
VN	Graphic Card Model	Graphic Card Model
VN	Graphic Card Series	Graphic Card Series
VN	Graphics Card Series	Graphics Card Series
VN	Graphics Memory	Graphics Memory
VN	Greases type	Greases type
VN	Gril Accessory Type	Gril Accessory Type
VN	Grilles & Grille Guards type	Grilles & Grille Guards type
VN	Grilles type	Grilles type
VN	Grinder Features	Grinder Features
VN	Grinder Type	Grinder Type
VN	Hair Accessories	Hair Accessories
VN	Hair Care Benefits	Hair Care Benefits
VN	Hair Care Ingredient	Hair Care Ingredient
VN	Hair Color Type	Hair Color Type
VN	Hair Dryer Features	Hair Dryer Features
VN	Hair Removal Features	Hair Removal Features
VN	Hair Removal Type	Hair Removal Type
VN	Hair Style Features	Hair Style Features
VN	Hand Orientation	Hand Orientation
VN	Hand Tools Type	Hand Tools Type
VN	Hard Drive Capacity	Hard Drive Capacity
VN	Hat Brim Styles	Hat Brim Styles
VN	Hat Style	Hat Style
VN	Headphone Accessories	Headphone Accessories
VN	Headphone Features	Headphone Features
VN	Health Benefit	Health Benefit
VN	Heel Height (cm)	Heel Height (cm)
VN	Height	Height
VN	Helmets Type	Helmets Type
VN	Hijab Style	Hijab Style
VN	Home Entertainment Features	Home Entertainment Features
VN	Hood type	Hood type
VN	Hoodie Style	Hoodie Style
VN	Hook Type	Hook Type
VN	House Slippers	House Slippers
VN	How to use	How to use
VN	Hubcap Size	Hubcap Size
VN	Hubcaps, Trim Rings & Hub Accessories type	Hubcaps, Trim Rings & Hub Accessories type
VN	Humidifier Type	Humidifier Type
VN	ISBN/ISSN	ISBN/ISSN
VN	ISO Rating	ISO Rating
VN	Ice Cream Format	Ice Cream Format
VN	Image Capture Resolution	Image Capture Resolution
VN	Images	Images
VN	Important Notice	Important Notice
VN	Ingredient	Ingredient
VN	Ingredients	Ingredients
VN	Inner Material	Inner Material
VN	Input Connectivity	Input Connectivity
VN	Input Tray Capacity	Input Tray Capacity
VN	Input Type	Input Type
VN	Input Voltage	Input Voltage
VN	Insect Control Type	Insect Control Type
VN	Installation	Installation
VN	Instrument Key	Instrument Key
VN	Instrument Range	Instrument Range
VN	Interest	Interest
VN	Interface type	Interface type
VN	Interior Accessories Material	Interior Accessories Material
VN	Internal Memory	Internal Memory
VN	Intimate Type	Intimate Type
VN	Inverter	Inverter
VN	Inverter Motor	Inverter Motor
VN	Io Ports	Io Ports
VN	Iron Type	Iron Type
VN	Is Unisex	Is Unisex
VN	Isofix	Isofix
VN	Issue	Issue
VN	Items per each	Items per each
VN	Jacket Closure Type	Jacket Closure Type
VN	Jacket Coat Style	Jacket Coat Style
VN	Jacket Material	Jacket Material
VN	Jar Material Type	Jar Material Type
VN	Jeans Features	Jeans Features
VN	Jeans Fit Type	Jeans Fit Type
VN	Jug Material	Jug Material
VN	Jug Material Type	Jug Material Type
VN	Jug Type	Jug Type
VN	Juicer Features	Juicer Features
VN	Karaoke Features	Karaoke Features
VN	Karaoke Type	Karaoke Type
VN	Kettle Features	Kettle Features
VN	Kettle Material	Kettle Material
VN	Key Type	Key Type
VN	Kid years	Kid years
VN	Kids Bed Design	Kids Bed Design
VN	Kids Bed Size	Kids Bed Size
VN	Kids Desk Features	Kids Desk Features
VN	Kids Desk Type	Kids Desk Type
VN	Kids Storage Type	Kids Storage Type
VN	Kids' Bike Age	Kids' Bike Age
VN	Kitchen Board Features	Kitchen Board Features
VN	Kitchen Board Materials	Kitchen Board Materials
VN	Kitchen Board Type	Kitchen Board Type
VN	Kitchen Fitting Type	Kitchen Fitting Type
VN	Kitchen Island Design	Kitchen Island Design
VN	Kitchen Island Features	Kitchen Island Features
VN	Kitchen Tapware Type	Kitchen Tapware Type
VN	Knife Accessory Type	Knife Accessory Type
VN	Knife Type	Knife Type
VN	La Liga Teams	La Liga Teams
VN	Labelmaker Printing Type	Labelmaker Printing Type
VN	Labelmaker Type	Labelmaker Type
VN	Ladder Type	Ladder Type
VN	Landline Features	Landline Features
VN	Language	Language
VN	Laptop Compartment	Laptop Compartment
VN	Laptop Friendly	Laptop Friendly
VN	Laptop Type	Laptop Type
VN	Laptop size	Laptop size
VN	Laundry Needs	Laundry Needs
VN	Length	Length
VN	Length (cm)	Length (cm)
VN	Length (inches)	Length (inches)
VN	Length of the vaccuum's cord (m)	Length of the vaccuum's cord (m)
VN	Lens Color	Lens Color
VN	Lens Diameter	Lens Diameter
VN	Lens Kit	Lens Kit
VN	Lens Model	Lens Model
VN	Lens Mount Compatibility	Lens Mount Compatibility
VN	Lens Pack Size	Lens Pack Size
VN	Lens colour	Lens colour
VN	Lens_Axis	Lens_Axis
VN	Lens_Pack_Size	Lens_Pack_Size
VN	License Plate Covers & Frames type	License Plate Covers & Frames type
VN	Lifetime (L)	Lifetime (L)
VN	Light Bulb Colour	Light Bulb Colour
VN	Light Bulb Type	Light Bulb Type
VN	Light Bulb Wattage	Light Bulb Wattage
VN	Light Bulb Wattage (w)	Light Bulb Wattage (w)
VN	Light Features	Light Features
VN	Light Type	Light Type
VN	Lightbulb Type	Lightbulb Type
VN	Lightbulb Wattage	Lightbulb Wattage
VN	Linen Accessory Type	Linen Accessory Type
VN	Linen Fabric	Linen Fabric
VN	Lingerie Style	Lingerie Style
VN	Lips Makeup Benefits	Lips Makeup Benefits
VN	Lips Makeup Finish	Lips Makeup Finish
VN	Liquid Capacity (OZ)	Liquid Capacity (OZ)
VN	Listed Year Season	Listed Year Season
VN	Listening Length	Listening Length
VN	Load Capacity (kilograms)	Load Capacity (kilograms)
VN	Location Address	Location Address
VN	Location City	Location City
VN	Lock Type	Lock Type
VN	Long Description (Lorikeet)	Long Description (Lorikeet)
VN	Lubricant type	Lubricant type
VN	Lug Nuts & Accessories type	Lug Nuts & Accessories type
VN	Luggage_Size	Luggage_Size
VN	Lumens (lm)	Lumens (lm)
VN	Lunch_Box_Tiers	Lunch_Box_Tiers
VN	MPN	MPN
VN	Magnification	Magnification
VN	Main diamond carat size	Main diamond carat size
VN	Main stone	Main stone
VN	Make	Make
VN	Mal Number	Mal Number
VN	Manufacture Type	Manufacture Type
VN	Manufacturing country	Manufacturing country
VN	Marker Type	Marker Type
VN	Mascara Benefits	Mascara Benefits
VN	Material	Material
VN	Material Composition	Material Composition
VN	Material Type	Material Type
VN	Mattress Construction	Mattress Construction
VN	Mattress_features	Mattress_features
VN	Max Print Resolution Color	Max Print Resolution Color
VN	Max TV Size	Max TV Size
VN	Maximum Aperture Range	Maximum Aperture Range
VN	Maximum Brightness	Maximum Brightness
VN	Maximum Operating Height (centimeters)	Maximum Operating Height (centimeters)
VN	Maximum Print Resolution	Maximum Print Resolution
VN	Maximum Resolution	Maximum Resolution
VN	Maximum child weight	Maximum child weight
VN	Maximum recommended age	Maximum recommended age
VN	Maximum recommended child weight	Maximum recommended child weight
VN	Measuring Tool Type	Measuring Tool Type
VN	Measuring Tools type	Measuring Tools type
VN	Meat Tool Type	Meat Tool Type
VN	Media Handling Capacity	Media Handling Capacity
VN	Media Player Type	Media Player Type
VN	Megapixels	Megapixels
VN	Memory Card Type	Memory Card Type
VN	Memory Size	Memory Size
VN	Men's Trend	Men's Trend
VN	Metal	Metal
VN	Metode Pengiriman	Metode Pengiriman
VN	Mic Accessories	Mic Accessories
VN	Mic Connectivity	Mic Connectivity
VN	Mic Types	Mic Types
VN	Mice Features	Mice Features
VN	Microphone Inputs	Microphone Inputs
VN	Microwave Capacity (L)	Microwave Capacity (L)
VN	Microwave Features	Microwave Features
VN	Microwave Type	Microwave Type
VN	Milk Formula Flavor	Milk Formula Flavor
VN	Milk Formula Form	Milk Formula Form
VN	Milk Formula Size	Milk Formula Size
VN	Milk Type	Milk Type
VN	Min Aperture	Min Aperture
VN	Minimum Delivery Acceptance (Days)	Minimum Delivery Acceptance (Days)
VN	Minimum recommended age	Minimum recommended age
VN	Mirror Features	Mirror Features
VN	Mirror Type	Mirror Type
VN	Mist_Modes	Mist_Modes
VN	Mixer Features	Mixer Features
VN	Mixer Type	Mixer Type
VN	Mnimum Delivery Acceptance (Days)	Mnimum Delivery Acceptance (Days)
VN	Model	Model
VN	Model Compatibility	Model Compatibility
VN	Model Compatibility for Mac	Model Compatibility for Mac
VN	Model Type	Model Type
VN	Monitor Feature	Monitor Feature
VN	Mono/Color	Mono/Color
VN	Motherboard Memory Technology	Motherboard Memory Technology
VN	Moto Battery Size	Moto Battery Size
VN	Moto Tire Sizes	Moto Tire Sizes
VN	Motor Type	Motor Type
VN	Motorcycle Make	Motorcycle Make
VN	Motorcycle Model	Motorcycle Model
VN	Mount Features	Mount Features
VN	Mount Type	Mount Type
VN	Mounting	Mounting
VN	Mounting Type	Mounting Type
VN	Movement	Movement
VN	Multimedia Playback Time	Multimedia Playback Time
VN	Multipack	Multipack
VN	Multipack Bundle	Multipack Bundle
VN	Multipack or Bundle	Multipack or Bundle
VN	Multiple USB Charging	Multiple USB Charging
VN	NAS Number of Bays	NAS Number of Bays
VN	Name	Name
VN	Name (English)	Name (English)
VN	Name of Sound Card	Name of Sound Card
VN	Neck Material	Neck Material
VN	Necklace length	Necklace length
VN	Neckline	Neckline
VN	Net Depth (mm)	Net Depth (mm)
VN	Net Height (mm)	Net Height (mm)
VN	Net Width (mm)	Net Width (mm)
VN	Network	Network
VN	Network Connections	Network Connections
VN	Nicotine Level	Nicotine Level
VN	No Of People	No Of People
VN	No of Pieces	No of Pieces
VN	No. of included Batteries	No. of included Batteries
VN	No_of_Brushing_Modes	No_of_Brushing_Modes
VN	Noise Level (dB)	Noise Level (dB)
VN	Non-stick coating	Non-stick coating
VN	Notebook Features	Notebook Features
VN	Notebook Type	Notebook Type
VN	Number of Attachments	Number of Attachments
VN	Number of Blades	Number of Blades
VN	Number of CPU cores	Number of CPU cores
VN	Number of Cameras Included	Number of Cameras Included
VN	Number of Disc	Number of Disc
VN	Number of Doors	Number of Doors
VN	Number of Drawers	Number of Drawers
VN	Number of Ethernet ports	Number of Ethernet ports
VN	Number of Fans	Number of Fans
VN	Number of Key	Number of Key
VN	Number of Memory Slots	Number of Memory Slots
VN	Number of Pieces in Set	Number of Pieces in Set
VN	Number of Ports	Number of Ports
VN	Number of SATA Cables	Number of SATA Cables
VN	Number of Seats	Number of Seats
VN	Number of Settings	Number of Settings
VN	Number of Sheets per Ream	Number of Sheets per Ream
VN	Number of Shelves	Number of Shelves
VN	Number of Sockets	Number of Sockets
VN	Number of Speed	Number of Speed
VN	Number of Speeds	Number of Speeds
VN	Number of Stiches	Number of Stiches
VN	Number of Tins	Number of Tins
VN	Number of Waffles	Number of Waffles
VN	Number of bottles	Number of bottles
VN	Number of channels	Number of channels
VN	Number of hobs	Number of hobs
VN	Number of mode	Number of mode
VN	Number of pages	Number of pages
VN	Number of pieces	Number of pieces
VN	Number of pills	Number of pills
VN	Number_of_Blades	Number_of_Blades
VN	Number_of_Camera	Number_of_Camera
VN	Number_of_Tins	Number_of_Tins
VN	Number_of_Window	Number_of_Window
VN	Nut Type	Nut Type
VN	Occasion	Occasion
VN	Oil Tool Type	Oil Tool Type
VN	Open Dimension	Open Dimension
VN	Operating System	Operating System
VN	Optical Disk Drive	Optical Disk Drive
VN	Optical Sensor Resolution (megapixels)	Optical Sensor Resolution (megapixels)
VN	Optical Zoom	Optical Zoom
VN	Oral Care Benefits	Oral Care Benefits
VN	Organic	Organic
VN	Orientation	Orientation
VN	Other Electrical Type	Other Electrical Type
VN	Ottoman Design	Ottoman Design
VN	Outdoor Chair Type	Outdoor Chair Type
VN	Outdoor Dining Type	Outdoor Dining Type
VN	Outdoor Power Tool Type	Outdoor Power Tool Type
VN	Outdoor Table Type	Outdoor Table Type
VN	Outer Material	Outer Material
VN	Output Connectivity	Output Connectivity
VN	Output Tray Capacity	Output Tray Capacity
VN	Oven Max Temperature	Oven Max Temperature
VN	Oven Toaster Features	Oven Toaster Features
VN	Overheat control function	Overheat control function
VN	PPI	PPI
VN	Pack	Pack
VN	Pack Size	Pack Size
VN	Pack Type	Pack Type
VN	Package Content	Package Content
VN	Package Height (cm)	Package Height (cm)
VN	Package Length (cm)	Package Length (cm)
VN	Package Weight (kg)	Package Weight (kg)
VN	Package Width (cm)	Package Width (cm)
VN	Packaging Type	Packaging Type
VN	Paint Accessory Type	Paint Accessory Type
VN	Paint Colour Tone	Paint Colour Tone
VN	Paint Finish	Paint Finish
VN	Paint Function	Paint Function
VN	Paint Product Range	Paint Product Range
VN	Paint Product Range Variation	Paint Product Range Variation
VN	Paint Surface Type	Paint Surface Type
VN	Paint Type	Paint Type
VN	Paint Volume (L)	Paint Volume (L)
VN	Paint/Stain Key Features	Paint/Stain Key Features
VN	Painting Category	Painting Category
VN	Paints & Primers type	Paints & Primers type
VN	Pan Type	Pan Type
VN	Pants Fly	Pants Fly
VN	Panty Type	Panty Type
VN	Paper Features	Paper Features
VN	Paper Handling	Paper Handling
VN	Paper Ply	Paper Ply
VN	Paper Quality (GSM)	Paper Quality (GSM)
VN	Paper Tray Capacity	Paper Tray Capacity
VN	Paper Type	Paper Type
VN	Parent facing	Parent facing
VN	Pasta Maker Tools	Pasta Maker Tools
VN	Pasta Tool Features	Pasta Tool Features
VN	Pattern	Pattern
VN	Pattern/Detail	Pattern/Detail
VN	Patterned	Patterned
VN	Pax	Pax
VN	Peeler Type	Peeler Type
VN	Pen Thickness	Pen Thickness
VN	Pen Type	Pen Type
VN	Pen_Thickness	Pen_Thickness
VN	Pencil Hardness	Pencil Hardness
VN	Pencil Type	Pencil Type
VN	Performance & Air Intakes type	Performance & Air Intakes type
VN	Peril Type	Peril Type
VN	Pet Food Bag Size	Pet Food Bag Size
VN	Pet Size	Pet Size
VN	Pets Flavor	Pets Flavor
VN	Phone Features	Phone Features
VN	Phone Type	Phone Type
VN	Pickup Configuration	Pickup Configuration
VN	Picture Size	Picture Size
VN	Picture_Frame_Art_Type	Picture_Frame_Art_Type
VN	Pillow Shape	Pillow Shape
VN	Pillowsbolsters Length	Pillowsbolsters Length
VN	Pillowsbolsters Width	Pillowsbolsters Width
VN	Pipe Fitting Type	Pipe Fitting Type
VN	Platform Type	Platform Type
VN	Plug Type	Plug Type
VN	Plumbing Components	Plumbing Components
VN	Plumbing Fixture Type	Plumbing Fixture Type
VN	Plumbing Tapware Features	Plumbing Tapware Features
VN	Plumbing Tapware Finish	Plumbing Tapware Finish
VN	Pointing Device	Pointing Device
VN	Pole_Material	Pole_Material
VN	Portable Speaker Features	Portable Speaker Features
VN	Ports	Ports
VN	Ports Input	Ports Input
VN	Pot Material	Pot Material
VN	Pot Rack Type	Pot Rack Type
VN	Power	Power
VN	Power (watt/horsepower)	Power (watt/horsepower)
VN	Power Adapter Type	Power Adapter Type
VN	Power Capacity	Power Capacity
VN	Power Consumption	Power Consumption
VN	Power Consumption (W)	Power Consumption (W)
VN	Power Lenses	Power Lenses
VN	Power Output (Amp)	Power Output (Amp)
VN	Power Output (W)	Power Output (W)
VN	Power Source Type	Power Source Type
VN	Power Steering type	Power Steering type
VN	Power Supply	Power Supply
VN	Power Tool Accessory Size (mm)	Power Tool Accessory Size (mm)
VN	Power Tool Accessory Type	Power Tool Accessory Type
VN	Power Tool Feature	Power Tool Feature
VN	Power Type	Power Type
VN	Power of Motor (Hp)	Power of Motor (Hp)
VN	Power source	Power source
VN	Power_Consumption_(W)	Power_Consumption_(W)
VN	Powerbank Capacity	Powerbank Capacity
VN	Powerbank Features	Powerbank Features
VN	Powerpoint Type	Powerpoint Type
VN	Premier League Teams	Premier League Teams
VN	Pressure Cooker Features	Pressure Cooker Features
VN	Price	Price
VN	Primary(Back) Camera Resolution	Primary(Back) Camera Resolution
VN	Print Speed	Print Speed
VN	Printer Connectivity Type	Printer Connectivity Type
VN	Printer Function Type	Printer Function Type
VN	Privacy	Privacy
VN	Processor	Processor
VN	Processor Frequency	Processor Frequency
VN	Processor Frequency (GHz)	Processor Frequency (GHz)
VN	Processor Type	Processor Type
VN	Product Dimension	Product Dimension
VN	Product Form	Product Form
VN	Product Height	Product Height
VN	Product Length	Product Length
VN	Product Options	Product Options
VN	Product Size	Product Size
VN	Product Tier	Product Tier
VN	Product Type	Product Type
VN	Product Volume	Product Volume
VN	Product width	Product width
VN	Product_License	Product_License
VN	Projector Features	Projector Features
VN	Projector Resolution	Projector Resolution
VN	Projector Type	Projector Type
VN	Protective Clothing Features	Protective Clothing Features
VN	Protective Shoe Features	Protective Shoe Features
VN	Provide Installation	Provide Installation
VN	Publisher	Publisher
VN	Pullers type	Pullers type
VN	Purification Capacity (CADR)	Purification Capacity (CADR)
VN	Purification Capacity (l/h)	Purification Capacity (l/h)
VN	Purification Method	Purification Method
VN	Purpose	Purpose
VN	Quantity	Quantity
VN	RAM memory	RAM memory
VN	RGB Lighting	RGB Lighting
VN	RPM	RPM
VN	Rack & Pinion type	Rack & Pinion type
VN	Racket Material	Racket Material
VN	Racquet Material	Racquet Material
VN	Racquet Stringing	Racquet Stringing
VN	Radio Features	Radio Features
VN	Radio Type	Radio Type
VN	Raise	Raise
VN	Range Mount Type	Range Mount Type
VN	Read Speed	Read Speed
VN	Receiver Features	Receiver Features
VN	Recommended Age	Recommended Age
VN	Recommended Gender	Recommended Gender
VN	Recommended Maximum Age	Recommended Maximum Age
VN	Recommended Minimum Age	Recommended Minimum Age
VN	Recommended User	Recommended User
VN	Recorder Channel Capacity	Recorder Channel Capacity
VN	Recorder Connectivity	Recorder Connectivity
VN	Recorder Types	Recorder Types
VN	Refills	Refills
VN	Refrigerator Features	Refrigerator Features
VN	Refrigerator Type	Refrigerator Type
VN	Reinforced_Toe_Cap	Reinforced_Toe_Cap
VN	Relays	Relays
VN	Replacement Type	Replacement Type
VN	Resolution	Resolution
VN	Response Time	Response Time
VN	Rice Cooker Features	Rice Cooker Features
VN	Rider_Height_(CM)	Rider_Height_(CM)
VN	Ring Size	Ring Size
VN	Roasting Tray Type	Roasting Tray Type
VN	Robot Vacuum Features	Robot Vacuum Features
VN	Room Size	Room Size
VN	Rug Material	Rug Material
VN	Rug Pile	Rug Pile
VN	Rug Shape	Rug Shape
VN	Rug Size	Rug Size
VN	Rug Thickness (mm)	Rug Thickness (mm)
VN	Rug Type	Rug Type
VN	Running Boards & Steps type	Running Boards & Steps type
VN	SIM card Slots	SIM card Slots
VN	SPF rating	SPF rating
VN	Safe type	Safe type
VN	Safety Feature	Safety Feature
VN	Salt & Pepper Tool Type	Salt & Pepper Tool Type
VN	Sandal Type	Sandal Type
VN	Sauces/Gravies/Marinades Type	Sauces/Gravies/Marinades Type
VN	Saw Type	Saw Type
VN	Saws Size	Saws Size
VN	Scan Resolution	Scan Resolution
VN	Scanner Function	Scanner Function
VN	Scarf Style	Scarf Style
VN	Scent	Scent
VN	Scent Feature	Scent Feature
VN	Screen Size	Screen Size
VN	Screen Size (inches)	Screen Size (inches)
VN	Screen Type	Screen Type
VN	Sealer Finish	Sealer Finish
VN	Sealer Product Range	Sealer Product Range
VN	Sealer Surface Type	Sealer Surface Type
VN	Sealer Usage	Sealer Usage
VN	Season	Season
VN	Secondary(Front) Camera Resolution	Secondary(Front) Camera Resolution
VN	Security Camera Features	Security Camera Features
VN	Security Camera Style	Security Camera Style
VN	Security System Type	Security System Type
VN	SellerSKU	SellerSKU
VN	Sensor Type	Sensor Type
VN	Series A Teams	Series A Teams
VN	Serveware Compartments	Serveware Compartments
VN	Service Provider	Service Provider
VN	Service Size	Service Size
VN	Services	Services
VN	Serving Bowl Type	Serving Bowl Type
VN	Serving Tool Type	Serving Tool Type
VN	Set Size	Set Size
VN	Settings	Settings
VN	Sewing Machine Features	Sewing Machine Features
VN	Sewing speed (Stiches per min)	Sewing speed (Stiches per min)
VN	Shade Fabric	Shade Fabric
VN	Shade Features	Shade Features
VN	Shaft material	Shaft material
VN	Shalat Style	Shalat Style
VN	Shape	Shape
VN	Shape of the watch case	Shape of the watch case
VN	Shaper Style	Shaper Style
VN	Shaver Features	Shaver Features
VN	Shaver Type	Shaver Type
VN	Shelf Design	Shelf Design
VN	Shelf Expiry	Shelf Expiry
VN	Shelters&Canopies_Type	Shelters&Canopies_Type
VN	Shocks, Struts & Suspension type	Shocks, Struts & Suspension type
VN	Shoe Type	Shoe Type
VN	Shoes Closure Type	Shoes Closure Type
VN	Shoes Decoration	Shoes Decoration
VN	Short Description	Short Description
VN	Signal Type	Signal Type
VN	Size	Size
VN	Size (feet)	Size (feet)
VN	Size Baby Clothing	Size Baby Clothing
VN	Size Baby Shoes	Size Baby Shoes
VN	Size Glove	Size Glove
VN	Size Helmet	Size Helmet
VN	Size Shoes	Size Shoes
VN	Size Stuffed Toys	Size Stuffed Toys
VN	Size Wear	Size Wear
VN	Size clothing	Size clothing
VN	Size of Beds	Size of Beds
VN	Size of the disc	Size of the disc
VN	Size_mm	Size_mm
VN	Skin Care Benefits	Skin Care Benefits
VN	Skin Concerns	Skin Concerns
VN	Skin Tone	Skin Tone
VN	Skin Type	Skin Type
VN	Skirt Length	Skirt Length
VN	Skirt Style	Skirt Style
VN	Sleep Style	Sleep Style
VN	Sleeping Capacity (number of persons)	Sleeping Capacity (number of persons)
VN	Sleeping_Bag_Shape	Sleeping_Bag_Shape
VN	Sleeve Length	Sleeve Length
VN	Sleeves	Sleeves
VN	Smart Glasses Features	Smart Glasses Features
VN	Smart TV OS	Smart TV OS
VN	Smartwear Size	Smartwear Size
VN	Sneaker Height	Sneaker Height
VN	Sneaker Type	Sneaker Type
VN	Sneaker Upper Height	Sneaker Upper Height
VN	Sneakers Style	Sneakers Style
VN	Snow Chains type	Snow Chains type
VN	Sock Tight Style	Sock Tight Style
VN	Sofa Type	Sofa Type
VN	Sold in	Sold in
VN	Soleplate Type	Soleplate Type
VN	Solution	Solution
VN	Speaker Configuration	Speaker Configuration
VN	Speaker Connectivity	Speaker Connectivity
VN	Speaker Features	Speaker Features
VN	Speaker Phone	Speaker Phone
VN	Special Feature	Special Feature
VN	Special Price	Special Price
VN	Specialty Cooking Utensil Type	Specialty Cooking Utensil Type
VN	Specialty Glass Type	Specialty Glass Type
VN	Specialty Pan Type	Specialty Pan Type
VN	Speed Class	Speed Class
VN	Speed of Processor (GHz)	Speed of Processor (GHz)
VN	Spice Tool Type	Spice Tool Type
VN	Spin Speed (RPM)	Spin Speed (RPM)
VN	Spinmop Features	Spinmop Features
VN	Spoilers, Wings & Styling Kits type	Spoilers, Wings & Styling Kits type
VN	Sport Water Bottle Capacity (litres)	Sport Water Bottle Capacity (litres)
VN	Sports Type	Sports Type
VN	Sports_Material	Sports_Material
VN	Staple Type	Staple Type
VN	Start date of promotion	Start date of promotion
VN	Steamer Material	Steamer Material
VN	Steamer Tiers	Steamer Tiers
VN	Steering & Suspension Tools type	Steering & Suspension Tools type
VN	Steering Wheels & Accessories type	Steering Wheels & Accessories type
VN	Sticky Label Feature	Sticky Label Feature
VN	Sticky Label Type	Sticky Label Type
VN	Stool Height	Stool Height
VN	Storage Capacity	Storage Capacity
VN	Storage Feature	Storage Feature
VN	Storage Guidelines	Storage Guidelines
VN	Storage Space	Storage Space
VN	Storage Tub Features	Storage Tub Features
VN	Storage Tub Type	Storage Tub Type
VN	Storage Type	Storage Type
VN	Storage Type Gr	Storage Type Gr
VN	Store	Store
VN	Stovetop Kettle Features	Stovetop Kettle Features
VN	Strainer Type	Strainer Type
VN	Strap Material	Strap Material
VN	Stringlights Length	Stringlights Length
VN	Stroke oils	Stroke oils
VN	Stroller brand compatibility	Stroller brand compatibility
VN	Stroller weight	Stroller weight
VN	Style	Style_translate
VN	Style Helmet	Style Helmet
VN	Stylus Features	Stylus Features
VN	Subscription	Subscription
VN	Subwoofer	Subwoofer
VN	Suction Power (kPa)	Suction Power (kPa)
VN	Suction_Power	Suction_Power
VN	Suitable Age	Suitable Age
VN	Sun protection range (SPF)	Sun protection range (SPF)
VN	Sunglasses lens type	Sunglasses lens type
VN	Swimwear Style	Swimwear Style
VN	Swimwear Type	Swimwear Type
VN	Switches	Switches
VN	System Memory	System Memory
VN	Số lượng	Số lượng
VN	TV  Installation	TV  Installation
VN	TV Adapter Type	TV Adapter Type
VN	TV Features	TV Features
VN	TV Installation	TV Installation
VN	TV Receiver	TV Receiver
VN	TV Resolution	TV Resolution
VN	TV Value Added Services	TV Value Added Services
VN	TV Value-Added Services	TV Value-Added Services
VN	Table Base	Table Base
VN	Table Features	Table Features
VN	Table Height	Table Height
VN	Tablet Connection	Tablet Connection
VN	Tablet Features	Tablet Features
VN	Tailored Nutrition	Tailored Nutrition
VN	Tank Capacity (L)	Tank Capacity (L)
VN	Tank_Capacity	Tank_Capacity
VN	Tap Filter Features	Tap Filter Features
VN	Tape Type	Tape Type
VN	Taxes	Taxes
VN	Tea Accessory Type	Tea Accessory Type
VN	Tea Format	Tea Format
VN	Tea Type	Tea Type
VN	Teapot Capacity (Cups)	Teapot Capacity (Cups)
VN	Technology	Technology
VN	Tee Neckline	Tee Neckline
VN	Tee Sleeve Length	Tee Sleeve Length
VN	Temperature_Rating	Temperature_Rating
VN	Thematic Graphic Design	Thematic Graphic Design
VN	Thermometer Features	Thermometer Features
VN	Thermometer Type	Thermometer Type
VN	Thickness (gsm)	Thickness (gsm)
VN	Thickness (mm)	Thickness (mm)
VN	Thread Count	Thread Count
VN	Throwing Hand	Throwing Hand
VN	Ticket Type	Ticket Type
VN	Tie Width	Tie Width
VN	Tile Type	Tile Type
VN	Timber Type	Timber Type
VN	Tire Model	Tire Model
VN	Tire Size	Tire Size
VN	Title	Title
VN	Toe Shape	Toe Shape
VN	Tonneau Covers type	Tonneau Covers type
VN	Tool Storage Type	Tool Storage Type
VN	Tool compatible with Surfaces:	Tool compatible with Surfaces:
VN	Tools Included	Tools Included
VN	Tools Power Source	Tools Power Source
VN	Top Style	Top Style
VN	Top Type	Top Type
VN	Top Types	Top Types
VN	Torque (lb-in)	Torque (lb-in)
VN	Total Capacity	Total Capacity
VN	Towel Material	Towel Material
VN	Towel Size	Towel Size
VN	Towel Thickness	Towel Thickness
VN	Towing Products & Winches type	Towing Products & Winches type
VN	Towing and Winches type	Towing and Winches type
VN	Toy Size	Toy Size
VN	Tracker Style	Tracker Style
VN	Trailer Accessories type	Trailer Accessories type
VN	Transmission & Parts type	Transmission & Parts type
VN	Transmission Speed (Mbps)	Transmission Speed (Mbps)
VN	Travel Size	Travel Size
VN	Tray	Tray
VN	Truck Bed & Tailgate type	Truck Bed & Tailgate type
VN	Turntable Type	Turntable Type
VN	Type	Type
VN	Type Air Conditioner	Type Air Conditioner
VN	Type Air Fresherner	Type Air Fresherner
VN	Type Care	Type Care
VN	Type Case/Cover	Type Case/Cover
VN	Type Concert Percussion	Type Concert Percussion
VN	Type Curtain	Type Curtain
VN	Type Digital	Type Digital
VN	Type Free	Type Free
VN	Type Gauges	Type Gauges
VN	Type Paint	Type Paint
VN	Type Seminar	Type Seminar
VN	Type Woodwinds	Type Woodwinds
VN	Type component switch	Type component switch
VN	Type of Animal	Type of Animal
VN	Type of Baby Carrier	Type of Baby Carrier
VN	Type of Battery	Type of Battery
VN	Type of Bird Cage Accessories	Type of Bird Cage Accessories
VN	Type of Bodywash	Type of Bodywash
VN	Type of Breastpumps	Type of Breastpumps
VN	Type of Camera Accessories	Type of Camera Accessories
VN	Type of Cat Toys	Type of Cat Toys
VN	Type of Courses	Type of Courses
VN	Type of Diaper Bags	Type of Diaper Bags
VN	Type of Dog Toys	Type of Dog Toys
VN	Type of Feeders	Type of Feeders
VN	Type of Fitness	Type of Fitness
VN	Type of Fitness Accessories	Type of Fitness Accessories
VN	Type of Juicer	Type of Juicer
VN	Type of Leash	Type of Leash
VN	Type of Material	Type of Material
VN	Type of Reptile Food	Type of Reptile Food
VN	Type of Reptile Habitats	Type of Reptile Habitats
VN	Type of Restaurant	Type of Restaurant
VN	Type of Rice Cooker	Type of Rice Cooker
VN	Type of Screen Guard	Type of Screen Guard
VN	Type of Small Pet Food	Type of Small Pet Food
VN	Type of Small Pet Habitat Accessories	Type of Small Pet Habitat Accessories
VN	Type of Spa/Beauty Service	Type of Spa/Beauty Service
VN	Type of Sport Accessories	Type of Sport Accessories
VN	Type of Sports	Type of Sports
VN	Type of Stroller	Type of Stroller
VN	Type of Tour/Travel	Type of Tour/Travel
VN	Type of Veterinary Diet	Type of Veterinary Diet
VN	Type of Washing Machine	Type of Washing Machine
VN	Type of blender	Type of blender
VN	Type of scanner	Type of scanner
VN	Type of shoe heel	Type of shoe heel
VN	Type of theme park	Type of theme park
VN	Type_of_Grinder	Type_of_Grinder
VN	Type_of_Material	Type_of_Material
VN	Types of S.T.E.M Toys	Types of S.T.E.M Toys
VN	Types of wipes	Types of wipes
VN	Types_of_Button	Types_of_Button
VN	USB Support	USB Support
VN	Umbrella Category	Umbrella Category
VN	Underwear Style	Underwear Style
VN	Unit Metric	Unit Metric
VN	Unit Quantity	Unit Quantity
VN	Universal	Universal
VN	Usage Contact Lens	Usage Contact Lens
VN	Utensil Features	Utensil Features
VN	Vacuum Cleaner Features	Vacuum Cleaner Features
VN	Valid From (dd/mm/yyyy)	Valid From (dd/mm/yyyy)
VN	Valid To (dd/mm/yyyy)	Valid To (dd/mm/yyyy)
VN	Vase & Vessels Material	Vase & Vessels Material
VN	Vehicle Type	Vehicle Type
VN	Version	Version
VN	Video Capture Resolution	Video Capture Resolution
VN	Video Output	Video Output
VN	Video Resolution	Video Resolution
VN	Video URL	Video URL
VN	View Finder	View Finder
VN	Vinyl Type	Vinyl Type
VN	Virtual Assistant	Virtual Assistant
VN	Virtual Reality Features	Virtual Reality Features
VN	Viscosity	Viscosity
VN	Voltage	Voltage
VN	Volume	Volume
VN	Volume (ml)	Volume (ml)
VN	Volumetric	Volumetric
VN	Volumn (ml)	Volumn (ml)
VN	Waist Type	Waist Type
VN	Wall Mount Features	Wall Mount Features
VN	Wall Oven Type	Wall Oven Type
VN	Wallet Type	Wallet Type
VN	Wardrobe Blocks	Wardrobe Blocks
VN	Wardrobe Door Type	Wardrobe Door Type
VN	Wardrobe Materials	Wardrobe Materials
VN	Warranty	Warranty
VN	Warranty Period	Warranty Period
VN	Warranty Policy	Warranty Policy
VN	Warranty Policy (English)	Warranty Policy (English)
VN	Warranty Type	Warranty Type
VN	Wash Color	Wash Color
VN	Washing Capacity (kg)	Washing Capacity (kg)
VN	Washing Cleaning Instruction	Washing Cleaning Instruction
VN	Washing Features	Washing Features
VN	Watch Connectivity	Watch Connectivity
VN	Watch Dial Size	Watch Dial Size
VN	Watch Features	Watch Features
VN	Watch Size	Watch Size
VN	Watch Strap Color	Watch Strap Color
VN	Watch glass material	Watch glass material
VN	Watch's features/functions	Watch's features/functions
VN	Water Dispenser Features	Water Dispenser Features
VN	Water Dispenser Type	Water Dispenser Type
VN	Water Efficiency (No of ticks)	Water Efficiency (No of ticks)
VN	Water Heater Features	Water Heater Features
VN	Water Heater Type	Water Heater Type
VN	Water Heating Energy	Water Heating Energy
VN	Water Holding Capacity (L)	Water Holding Capacity (L)
VN	Water Resistance	Water Resistance
VN	Water Resistant	Water Resistant
VN	Water Tank Capacity (L)	Water Tank Capacity (L)
VN	Water_Resistance_Level	Water_Resistance_Level
VN	Water_Tank_Capacity	Water_Tank_Capacity
VN	Waterproof	Waterproof
VN	Wattage	Wattage
VN	Wattage (W)	Wattage (W)
VN	Weighing scale maximum	Weighing scale maximum
VN	Weight	Weight
VN	Weight (Kgs)	Weight (Kgs)
VN	Weight (kg)	Weight (kg)
VN	Weight Capacity	Weight Capacity
VN	Weight Type	Weight Type
VN	Weight of precious metal	Weight of precious metal
VN	Weight or age range	Weight or age range
VN	Welder Type	Welder Type
VN	What's in the box	What's in the box
VN	What's_in_the_box	What's_in_the_box
VN	Wheel Bolt-Pattern	Wheel Bolt-Pattern
VN	Wheel Diameter (inches)	Wheel Diameter (inches)
VN	Wheel Material	Wheel Material
VN	Wheel Offset (mm)	Wheel Offset (mm)
VN	Wheel PCD (mm)	Wheel PCD (mm)
VN	Wheel Width (inches)	Wheel Width (inches)
VN	Wheel_size	Wheel_size
VN	Wheels	Wheels
VN	Wheels Size	Wheels Size
VN	Wheels Type	Wheels Type
VN	Where is the watch movement made	Where is the watch movement made
VN	Where to wear it	Where to wear it
VN	Width	Width
VN	Width (cm)	Width (cm)
VN	Width (inches)	Width (inches)
VN	Window Hardware Type	Window Hardware Type
VN	Wine Glass Type	Wine Glass Type
VN	Wings	Wings
VN	Wireless	Wireless
VN	Wireless Charging	Wireless Charging
VN	Wireless Charging Type	Wireless Charging Type
VN	Wireless Signal Range	Wireless Signal Range
VN	Wireless Transmission Speed (Mbps)	Wireless Transmission Speed (Mbps)
VN	Women's Trend	Women's Trend
VN	Womens Trend	Womens Trend
VN	Woofer Size	Woofer Size
VN	Worklight Type	Worklight Type
VN	Writing Speed	Writing Speed
VN	Year	Year
VN	Year of publication	Year of publication
VN	Yoga Mat Feature	Yoga Mat Feature
VN	__images__	__images__
VN	about_product	about_product
VN	activity_type	activity_type
VN	artificial_plant_type	artificial_plant_type
VN	auto_battery_size	auto_battery_size
VN	bag_shape	bag_shape
VN	ball_size	ball_size
VN	bookcase_design	bookcase_design
VN	bulb_socket_type	bulb_socket_type
VN	car_model	car_model
VN	clothing_material	clothing_material
VN	coffee_machine_capacity	coffee_machine_capacity
VN	collar_type	collar_type
VN	color_family	color_family
VN	color_thumbnail	color_thumbnail
VN	coloured_gems_type	coloured_gems_type
VN	cookware_feature	cookware_feature
VN	curtain_material	curtain_material
VN	customes_themes	customes_themes
VN	denomination_dg	denomination_dg
VN	dimensions_rm	dimensions_rm
VN	dinnerware_plate_type	dinnerware_plate_type
VN	fa_create_year	fa_create_year
VN	fa_season	fa_season
VN	fan_features	fan_features
VN	filter_type	filter_type
VN	footwear_size	footwear_size
VN	footwear_type	footwear_type
VN	glassware_jug_type	glassware_jug_type
VN	glassware_material	glassware_material
VN	hair_style_features	hair_style_features
VN	hats_style	hats_style
VN	hdd_size	hdd_size
VN	home_fragrance_type	home_fragrance_type
VN	horsepower	horsepower
VN	inclination	inclination
VN	induction_cooker_features	induction_cooker_features
VN	input voltage (V)	input voltage (V)
VN	is_digital	is_digital
VN	is_unisex	is_unisex
VN	items_per_each	items_per_each
VN	jewellery Packaging and Display Type	jewellery Packaging and Display Type
VN	jewellery tool & equipment type	jewellery tool & equipment type
VN	kid_years	kid_years
VN	la_installation	la_installation
VN	laptop_compartment	laptop_compartment
VN	light_bulb_type	light_bulb_type
VN	location_city	location_city
VN	mahp or mahs	mahp or mahs
VN	material_type	material_type
VN	motorcycle_model	motorcycle_model
VN	no_of_people	no_of_people
VN	number of items selling in the SKU	number of items selling in the SKU
VN	number_of_hobs	number_of_hobs
VN	number_of_pieces	number_of_pieces
VN	outdoor Power Tool Accessory	outdoor Power Tool Accessory
VN	package_content	package_content
VN	package_height	package_height
VN	package_length	package_length
VN	package_weight	package_weight
VN	package_width	package_width
VN	pet_size	pet_size
VN	power_consumption	power_consumption
VN	power_lenses	power_lenses
VN	product_type	product_type
VN	range_hood_features	range_hood_features
VN	recommended_gender	recommended_gender
VN	size_baby_clothing	size_baby_clothing
VN	size_wear	size_wear
VN	sms or email	sms or email
VN	sskTestProperty	sskTestProperty
VN	steamer_features	steamer_features
VN	storage_feature	storage_feature
VN	test_multi_text_attribute	test_multi_text_attribute
VN	test_sku_value	test_sku_value
VN	test_value_normalization	test_value_normalization
VN	thickness of mattress	thickness of mattress
VN	time slot	time slot
VN	tires_variation	tires_variation
VN	towel_fabric	towel_fabric
VN	transmission_type	transmission_type
VN	type_digital	type_digital
VN	type_tools	type_tools
VN	unit_metric	unit_metric
VN	upholstery	upholstery
VN	usage_contact_lens	usage_contact_lens
VN	warranty_type	warranty_type
VN	watch_strap_color	watch_strap_color
VN	water_resistance	water_resistance
VN	water_resistant	water_resistant
VN	wattage_ha	wattage_ha
VN	weight_of_metal	weight_of_metal
VN	wiper_size	wiper_size

dicMap={}
for line in  lines.split("\n"):
    arr = line.split("\t")
    if len(arr)==3:
       dicMap[arr[1].strip()] = arr[2].strip()+"_translate"




write_data_to_xls(file_name='lazada_vn_attrs.xls',dicMap=dicMap,title=['站点',"属性标记","属性翻译"],site="VN")
'''
