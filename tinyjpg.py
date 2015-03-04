import urllib2
import glob
import base64

API_KEY = 'kusRBnuU1u0e7NCMSCGw5SUZHscYH34a'

encoded_auth = base64.b64encode('api:%s' % API_KEY)

jpg_files_to_compress = glob.glob('originals/*.jpg')
png_files_to_compress = glob.glob('originals/*.png')
files_to_compress = jpg_files_to_compress + png_files_to_compress

for filepath in files_to_compress:
  file_data = open(filepath, 'rb').read()
  file_name = filepath.split('/')[1]
  request = urllib2.Request('https://api.tinypng.com/shrink', file_data)
  request.add_header('Authorization', 'Basic %s' % encoded_auth)

  response = urllib2.urlopen(request)

  if response.getcode() == 201:
    compressed_location = response.info().getheaders('Location')[0]
    compressed_data = urllib2.urlopen(compressed_location).read()
    open('compressed/%s' % file_name, 'wb').write(compressed_data)
    print "Success: %s" % file_name
  else:
    print "FAIL: %s" % file_name