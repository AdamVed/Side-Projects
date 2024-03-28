import os
import time
import datetime

ignore_list = ["Sort.lnk","ini", "!Folders", "junk_sorter.pyw", "junk_sorter.py"]
extensions = ['264', '3g2', '3gp', 'arf', 'asf', 'asx', 'avi', 'bik', 'dash', 'dat', 'dvr', 'flv', 'h264', 'm2t', 'm2ts', 'm4v', 'mkv', 'mod', 'mov', 'mp4', 'mpeg', 'mpg', 'mts', 'ogv', 'prproj', 'rec', 'rmvb', 'swf', 'tod', 'tp', 'ts', 'vob', 'webm', 'wlmp', 'wmv', '3ga', 'aac', 'aiff', 'amr', 'ape', 'arf', 'asf', 'asx', 'cda', 'dvf', 'flac', 'gp4', 'gp5', 'gpx', 'logic', 'm4a', 'm4b', 'm4p', 'midi', 'mp3', 'ogg', 'opus', 'pcm', 'rec', 'snd', 'sng', 'uax', 'wav', 'wma', 'wpl', 'zab', 'bmp', 'cpt', 'dds', 'dib', 'dng', 'emf', 'gif', 'heic', 'ico', 'icon', 'jpeg', 'jpg', 'pcx', 'pic', 'png', 'psd', 'psdx', 'raw', 'tga', 'thm', 'tif', 'tiff', 'wbmp', 'wdp', 'webp', 'arw', 'cr2', 'crw', 'dcr', 'dng', 'fpx', 'mrw', 'nef', 'orf', 'pcd', 'ptx', 'raf', 'raw', 'rw2', 'ai', 'cdr', 'csh', 'csl', 'drw', 'emz', 'odg', 'pic', 'sda', 'svg', 'svgz', 'swf', 'wmf', 'abr', 'aep', 'ai', 'ani', 'cdt', 'djvu', 'eps', 'fla', 'icns', 'ico', 'icon', 'mdi', 'odg', 'pic', 'psb', 'psd', 'pzl', 'sup', 'vsdx', 'xmp', '3d', '3ds', 'c4d', 'dgn', 'dwfx', 'dwg', 'dxf', 'ipt', 'lcf', 'max', 'obj', 'pro', 'skp', 'stl', 'u3d', 'x_t', 'eot', 'otf', 'ttc', 'ttf', 'woff', 'abw', 'aww', 'chm', 'cnt', 'dbx', 'djvu', 'doc', 'docm', 'docx', 'dot', 'dotm', 'dotx', 'epub', 'gp4', 'ind', 'indd', 'key', 'keynote', 'mht', 'mpp', 'odf', 'ods', 'odt', 'opx', 'ott', 'oxps', 'pages', 'pdf', 'pmd', 'pot', 'potx', 'pps', 'ppsx', 'ppt', 'pptm', 'pptx', 'prn', 'prproj', 'ps', 'pub', 'pwi', 'rtf', 'sdd', 'sdw', 'shs', 'snp', 'sxw', 'tpl', 'vsd', 'wpd', 'wps', 'wri', 'xps', '1st', 'alx', 'application', 'asp', 'csv', 'htm', 'html', 'log', 'lrc', 'lst', 'md', 'nfo', 'opml', 'plist', 'reg', 'rtf', 'srt', 'sub', 'tbl', 'text', 'txt', 'xml', 'xmp', 'xsd', 'xsl', 'xslt', 'azw', 'azw3', 'azw4', 'cbr', 'cbz', 'epub', 'fb2', 'iba', 'ibooks', 'lit', 'mobi', 'pdf', 'numbers', 'ods', 'sdc', 'sxc', 'xls', 'xlsm', 'xlsx', 'accdb', 'accdt', 'doc', 'docm', 'docx', 'dot', 'dotm', 'dotx', 'mdb', 'mpd', 'mpp', 'mpt', 'oft', 'one', 'onepkg', 'pot', 'potx', 'pps', 'ppsx', 'ppt', 'pptm', 'pptx', 'pst', 'pub', 'snp', 'thmx', 'vsd', 'vsdx', 'xls', 'xlsm', 'xlsx', 'big', 'bik', 'cab', 'dat', 'dds', 'hi', 'lng', 'pak', 'replay', 'replay', 'res', 'rofl', 'sav', 'save', 'sc2replay', 'scn', 'scx', 'uax', 'wotreplay', 'wowpreplay', 'wrpl', 'dat', 'g64', 'gb', 'gba', 'mbz', 'n64', 'nds', 'nes', 'rom', 'smc', 'smd', 'srm', 'v64', 'ova', 'ovf', 'pvm', 'vdi', 'vhd', 'vhdx', 'vmdk', 'vmem', 'vmwarevm', 'vmx', 'ashx', 'asp', 'aspx', 'atom', 'bc', 'bc!', 'class', 'crdownload', 'css', 'dlc', 'download', 'download', 'eml', 'flv', 'gdoc', 'gif', 'gsheet', 'gslides', 'htm', 'html', 'js', 'json', 'jsp', 'jws', 'mht', 'opml', 'part', 'partial', 'php', 'png', 'rss', 'swf', 'torrent', 'webm', 'webp', 'xap', 'xhtml', 'xml', 'xsd', 'xsl', 'xslt', 'dbx', 'eml', 'ldif', 'mht', 'msg', 'pst', 'vcf', 'app', 'asp', 'bat', 'chm', 'cnt', 'com', 'eml', 'exe', 'gadget', 'inf', 'js', 'lnk', 'mdb', 'msi', 'prg', 'reg', 'scr', 'shs', 'tmp', 'vbs', 'bat', 'bin', 'chm', 'class', 'com', 'dll', 'drv', 'exe', 'jar', 'js', 'lnk', 'ocx', 'pcx', 'scr', 'shs', 'swf', 'sys', 'vbs', 'vxd', 'wmf', 'ccc', 'cerber', 'cerber2', 'crypt', 'cryptolocker', 'cryptowall', 'ecc', 'ezz', 'locky', 'micro', 'zepto', '001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '7z', '7z.001', '7z.002', '7z.003', '7z.004', '7zip', 'a00', 'a01', 'a02', 'a03', 'a04', 'a05', 'ace', 'air', 'appxbundle', 'arc', 'arj', 'asec', 'bar', 'bin', 'c00', 'c01', 'c02', 'c03', 'cab', 'cbr', 'cbz', 'cso', 'deb', 'dlc', 'gz', 'gzip', 'hqx', 'inv', 'ipa', 'isz', 'jar', 'msix', 'msu', 'nbh', 'pak', 'part1.exe', 'part1.rar', 'part2.rar', 'pkg', 'pkg', 'r00', 'r01', 'r02', 'r03', 'r04', 'r05', 'r06', 'r07', 'r08', 'r09', 'r10', 'rar', 'rpm', 'sis', 'sisx', 'sit', 'sitd', 'sitx', 'tar', 'tar.gz', 'tgz', 'uax', 'vsix', 'webarchive', 'xap', 'z01', 'z02', 'z03', 'z04', 'z05', 'zab', 'zip', 'zipx', 'bak', 'bbb', 'bkf', 'bkp', 'dbk', 'gho', 'ipd', 'iso', 'json', 'mdbackup', 'nba', 'nbf', 'nco', 'nrg', 'old', 'rar', 'sbf', 'sbu', 'spb', 'spba', 'tib', 'wbcat', 'zip', '000', 'bin', 'ccd', 'cue', 'daa', 'dao', 'dmg', 'img', 'img', 'iso', 'isz', 'mdf', 'mds', 'mdx', 'nrg', 'tao', 'tc', 'toast', 'uif', 'vcd', 'apk', 'asec', 'bbb', 'crypt', 'crypt14', 'crypt15', 'ipa', 'ipd', 'ipsw', 'lqm', 'mdbackup', 'nbh', 'nomedia', 'npf', 'pkpass', 'rem', 'rsc', 'sbf', 'sis', 'sisx', 'spd', 'thm', 'tpk', 'vcf', 'xap', 'xapk', 'aac', 'aiff', 'amr', 'djr', 'm4a', 'midi', 'mp3', 'wav', 'wma', 'gdb', 'ofx', 'qif', 'accdb', 'accdt', 'csv', 'db', 'dbf', 'fdb', 'gdb', 'idx', 'mdb', 'mdf', 'sdf', 'sql', 'sqlite', 'wdb', 'xml', 'adf', 'geo', 'gpx', 'kml', 'kmz', 'map', 'air', 'app', 'application', 'appx', 'bat', 'bin', 'com', 'cpl', 'deb', 'dll', 'elf', 'exe', 'jar', 'js', 'lnk', 'msi', 'part1.exe', 'prg', 'rpm', 'shs', 'vbs', 'xap', 'alx', 'blf', 'cpl', 'dat', 'dll', 'drv', 'ds_store', 'dump', 'evtx', 'gadget', 'idx', 'inf', 'kext', 'key', 'mui', 'ocx', 'reg', 'rom', 'scr', 'sfcache', 'swp', 'sys', 'vxd', 'aae', 'alx', 'ccd', 'cnf', 'contact', 'cue', 'deskthemepack', 'eng', 'ics', 'ifo', 'lnk', 'lrtemplate', 'm3u', 'm3u8', 'mui', 'plist', 'pls', 'pro', 'ref', 'skn', 'svp', 'theme', 'themepack', 'thm', 'thmx', 'trm', 'usr', 'wba', 'crx', 'plugin', 'safariextz', 'vsix', 'xpi', 'asm', 'asp', 'aspx', 'bat', 'htm', 'inc', 'jad', 'java', 'js', 'json', 'jsp', 'lib', 'o', 'php', 'rc', 'rss', 'scpt', 'src', 'vbs', 'xcodeproj', 'xml', 'xsd', 'xsl', 'xslt', 'cfg', 'cnf', 'config', 'ini', 'pro', 'reg', 'dmp', 'log', 'asec', 'crypt', 'key', 'ksd', 'pfx', 'pkpass', 'rem', 'tc', '!ut', 'adadownload', 'bc', 'bc!', 'blf', 'cache', 'crdownload', 'dmp', 'download', 'download', 'download', 'part', 'partial', 'tmp', '2023', '3dr', 'cal', 'dat', 'dct', 'dic', 'dmp', 'lng', 'log', 'md5', 'msmessagestore', 'mswmm', 'npo', 'prj', 'rep', 'rsc', 'srg', 'tbl', 'template', 'upd', 'upg']

img_group = ["jpg", "jpeg", "png"]
img_group_name = "images"

doc_group = ["docx", "rtf"]
doc_group_name = "word"

audio_group = ["m4a", "mp3", "mp4"]
audio_group_name = "audio"

video_group = ["mkv", "avi"]
video_group_name = "video"

file_groups = img_group + doc_group + audio_group + video_group

ignore_list.append(img_group_name)
ignore_list.append(doc_group_name)
ignore_list.append(audio_group_name)
ignore_list.append(video_group_name)


def getExtension(filename):
    return filename.split(".")[-1].lower()


def isFolderExists(extension):
    for filename in os.listdir():
        if extension.lower() == filename.lower():
            return True
    return False


def timestamp():
    dayMonthYear = f"[{datetime.datetime.now().day}-{datetime.datetime.now().month}-{datetime.datetime.now().year}]"
    hourMinuteSecond = f"[{datetime.datetime.now().hour}-{datetime.datetime.now().minute}-{datetime.datetime.now().second}]"
    return dayMonthYear + "  " + hourMinuteSecond


def verifyVitalFolders():
    isFolders = False
    for filename in os.listdir():
        if filename == "!Folders":
            return True
    os.mkdir("!Folders")
    
def getExtensionByGroup(extension):
        if extension in img_group:
            extension = img_group_name
            
        if extension in doc_group:
            extension = doc_group_name
            
        if extension in audio_group:
            extension = audio_group_name
            
        if extension in video_group:
            extension = video_group_name
            
        return extension

def run():
    verifyVitalFolders()
    
    # Ignore folders and the script itself 
    for filename in os.listdir():
        if filename in ignore_list or filename in extensions:
            continue

        if not os.path.isfile(filename):
            target_file_path = f"!Folders/{filename}"
            count = 0
            
            while os.path.exists(target_file_path):
                count += 1
                target_file_path = f"!Folders/{filename} - Copy ({count})"
        
            os.rename(filename, target_file_path)
            
            continue

        extension = getExtension(filename)
        
        if extension in ignore_list:
            continue
            
        if extension in file_groups:    
            extension = getExtensionByGroup(extension)
            
        # If we already have a folder called "pdf" then move the .pdf file there
        if isFolderExists(extension):
            target_file_path = f'{extension}/{filename}'
            count = 0
            
            # As long as we have a copy of a file in the target path, keep looping and incrementing count until we have a unique name
            while os.path.exists(target_file_path):
                count += 1
                base_name, orig_extension = os.path.splitext(filename)
                new_file_name = f"{base_name} - Copy ({count}){orig_extension}"
                target_file_path = f'{extension}/{new_file_name}'

            os.rename(filename, target_file_path)

        # If this is a new extension kind then first make a new folder for that extension and then move the file there
        else:
            os.mkdir(f'{extension}')
            os.rename(filename, f'{extension}/{filename}')
    print(timestamp())


run()
