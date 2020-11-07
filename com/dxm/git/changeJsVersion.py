
lines='''
    String commJsVer= "11.9";
    String inventoryJsVer   = "9.1";
    String productCommJsVer   = "11.0";
    String shopeeJsVer= "13.6";
    String lazadaJsVer= "12.1";
    String tokopediaJsVer= "8.9";
    String sendoJsVer= "1.9";
    String templateJsVer= "1.9";
    String crawlJsVer= "8.9";
    String moveJsVer= "8.4";
    String orderJsVar   = "11.5";
    String orderTrack   = "3.1";
    String settingsJsVer   = "9.5";
    String dashboardJsVer   = "7.8";
    String indexJsVer   = "8.0";
    String messageJsVer   = "1.6";
    String manisfestJsVer   = "1.8";
    String statisJsVer   = "1.0";
//项目css (css/*.css)
    String commCssVer   = "13.5";
    String productCommCssVer   = "11.1";
    String crawlCssVer   = "9.0";
    String shopeeCssVer= "9.8";
    String lazadaCssVer   = "9.7";
    String tokopediaCssVer   = "5.8";
    String sendoCssVer   = "0.9";
    String templateCssVer   = "2.0";
    String orderCssVer   = "10.4";
    String settingsCssVer   = "8.2";
    String dashboardCssVer   = "8.3";
    String indexCssVer   = "8.3";
    String inventoryCssVer   = "7.4";
    String messageCssVer   = "1.9";
    String statisCssVer   = "0.8";

//自写组件用
//  js/plugins/image_upload/upload.js
//  js/plugins/combobox/combobox.js
//  js/plugins/picZoom/picZoom.js
//  js/plugins/validform/validform.js
//  js/plugins/tagsForm/tags.js
    String componentsVer   = "4.0";

//框架、插件类 (js/plugins/*;  js/com/jq.js;  frame/*;)
    String pluginVer   = "3.6";
//插件edit文件(ckeditor/smEdit.css;  ckeditor/smEdit.js; )
    String pluginEditVer   = "2.7";
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