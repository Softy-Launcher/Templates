
def create():
	name = raw_input("Template name: ")
	theme = raw_input("Template Theme: (light/dark) ")
	summary = raw_input("Template Summary: ")
	back = raw_input("Template background: ")
	fore = raw_input("Template foreground: ")
	min_version = raw_input("Minimum Softy Version: ")
	store_to = raw_input("Where to store (on PC): ")
	xml_name = raw_input("xml name (without .xml) : ")
		
	xml = open(store_to+"/"+xml_name+".xml","w")
	xml.write('<?xml version="1.0" encoding="utf-8" ?>\n')
	xml.write('	<Softy>\n')
	xml.write('		<Info type="Template">\n')
	xml.write('			<Softy.NAME>'+name+'</Softy.NAME>\n')
	xml.write('			<Softy.BACK>'+back+'</Softy.BACK>\n')
	xml.write('			<Softy.FORE>'+fore+'</Softy.FORE>\n')
	xml.write('			<Softy.SUMMARY>'+summary+'</Softy.SUMMARY>\n')
	xml.write('			<Softy.MIN_VERSION>'+min_version+'</Softy.MIN_VERSION>\n')
	xml.write('			<Softy.THEME>'+theme+'</Softy.THEME>\n')
	xml.write('		</Info>\n')
	xml.write('	</Softy>\n')
	
	xml.close()
	
create()
