select * from eav_attribute where attribute_id =155 
select * from catalog_product_entity_text where attribute_id =155 
select * from eav_attribute_option where attribute_id =155 
select distinct option_id,value from eav_attribute_option_value where option_id in (187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207)
product_id = self.get_map_field_by_src(self.TYPE_PRODUCT, convert['id'], convert['code'])
		attribute_id = 155
		tags_dict={
			"AspenValley":"187",
			"Atmos":"188",
			"Broad Spectrum":"189",
			"CannaBees":"190",
			"CBD":"191",
			"CBDLiving":"192",
			"CBG":"193",
			"CBN":"194",
			"Delta 10 THC":"195",
			"Delta 8 THC":"196",
			"Delta 9 THC":"197",
			"Full Spectrum":"198",
			"GHC":"199",
			"Green Herbal Care":"200",
			"HempZilla":"201",
			"HHC":"202",
			"Hometown Hero":"203",
			"Isolate":"204",
			"Koi":"205",
			"RAW":"206",
			"THC O":"207",
}		
		tag_ids= list()
		for tag in convert["tags"].split(","):
			tag_id=tags_dict.get(tag)
			if tag_id:
				tag_ids.append(tag_id)
		tag_ids = ",".join(tag_ids)	
		self.log(tag_ids,"tag_ids")
		response_select=self.import_data_connector(self.create_select_query_connector('catalog_product_entity_text',{'entity_id': product_id,"attribute_id":attribute_id}))
		self.log(response_select,"response_select")
		if response_select:
			response_update=self.import_data_connector(self.create_update_query_connector('catalog_product_entity_text',{'value': tag_ids}, {'entity_id': product_id,"attribute_id":attribute_id}))
			self.log(response_update,"response_update")
		else:
			tags_product_data={
				"attribute_id":155,
				"store_id":0,
				"entity_id":product_id,
				"value":tag_ids
			}
			response_insert = self.import_data_connector(self.create_insert_query_connector('catalog_product_entity_text', tags_product_data))
			self.log(response_insert,"response_insert")
			if not response_insert:
				self.log(convert,"cannot_import")
		return self.get_map_field_by_src(self.TYPE_PRODUCT, convert['id'], convert['code'])
