
lines='''
//项目js 根据模块定
    String commJsVer  = "11.4";
    String inventoryJsVer  = "9.0";
    String productCommJsVer  = "10.7";
    String shopeeJsVer  = "13.0";
    String lazadaJsVer  = "11.7";
    String tokopediaJsVer  = "8.5";
    String sendoJsVer  = "1.2";
    String templateJsVer  = "1.7";
    String crawlJsVer  = "8.6";
    String moveJsVer  = "8.1";
    String orderJsVar  = "11.4";
    String orderTrack  = "3.0";
    String settingsJsVer  = "9.4";
    String dashboardJsVer  = "7.7";
    String indexJsVer  = "7.9";
    String messageJsVer  = "1.5";
    String manisfestJsVer  = "1.7";
    String statisJsVer  = "0.9";
//项目css (css/*.css)
    String commCssVer  = "13.3";
    String productCommCssVer  = "10.9";
    String crawlCssVer  = "8.8";
    String shopeeCssVer  = "9.5";
    String lazadaCssVer  = "9.5";
    String tokopediaCssVer  = "5.6";
    String sendoCssVer  = "0.7";
    String templateCssVer  = "1.9";
    String orderCssVer  = "10.3";
    String settingsCssVer  = "8.1";
    String dashboardCssVer  = "8.2";
    String indexCssVer  = "8.2";
    String inventoryCssVer  = "7.3";
    String messageCssVer  = "1.8";
    String statisCssVer  = "0.7";

//自写组件用
//  js/plugins/image_upload/upload.js
//  js/plugins/combobox/combobox.js
//  js/plugins/picZoom/picZoom.js
//  js/plugins/validform/validform.js
//  js/plugins/tagsForm/tags.js
    String componentsVer  = "3.9";

//框架、插件类 (js/plugins/*;  js/com/jq.js;  frame/*;)
    String pluginVer  = "3.5";
//插件edit文件(ckeditor/smEdit.css;  ckeditor/smEdit.js; )
    String pluginEditVer  = "2.6";
'''

for line in lines.split("\n"):
    line2 = line.strip()
    if line2.startswith("//"):
        print(line)
        continue
    elif len(line2)==0:
        print(line)
        continue
    arr=line.split("=")
    #print(line)
    version = float(arr[1].strip().replace("\"","").replace(";",""))
    #print(version,version+0.1)
    print("{} = \"{}\";".format(arr[0],round(version+0.1,2)  ))