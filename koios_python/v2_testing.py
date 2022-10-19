import urls as u
import epoch as ep


print("------------------------------------------------------------------MAINNET-------------------------------------------------------------------------------")

url = u.URLs().epoch_info_url()

print('\n')

ep.get_epoch_info(url=url)

print('\n')

ep.get_epoch_info(url=url, epoch_no=320)

print('------------------------------------------------------------------Custom Endpoint-----------------------------------------------------------------------')
print('\n')


url_custom = u.URLs(url="https://koios-otg.tosidrop.io/api/v0/").epoch_info_url()

ep.get_epoch_info(url=url_custom, epoch_no=320)

print('\n')

print('------------------------------------------------------------------TESTNET-------------------------------------------------------------------------------')
print('\n')

url_testnet = u.URLs(network='testnet').epoch_info_url()

ep.get_epoch_info(url=url_testnet, epoch_no=185)

print('\n')