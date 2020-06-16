#!/usr/bin/python2
import retrieval.uk_check_xml
import call_check.find_product_ids
import os
import time

def main():

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    uk_check_s3 = retrieval.uk_check_xml.CheckXML(base_dir)
    id_dict = uk_check_parse()
    platform_call = call_check.find_ids.FindIds(ID_dict, base_dir)
    urls = cplatform_call.url_json()
    platform_call.call_check(urls)



if __name__=="__main__":
    main()
