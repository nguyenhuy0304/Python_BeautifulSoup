import bs4
import requests

# Đóng gói hàm lấy tên sản phẩm và Rating:
def get_product_info(url):
    try:
        res = requests.get(url)
        # Đọc dữ liệu có được từ việc truy cập vào url:
        soup = bs4.BeautifulSoup(res.content, 'html.parser')

        # Trích xuất từ Tag của BeautifulSoup:

        product_title = soup.find('h1', attrs={'class': 'pdp-mod-product-badge-title'}).text.strip()
        product_rating = str(
            soup.find('div', attrs={'class': 'container-star pdp-review-summary__stars pdp-stars_size_s'})).count(
            '<img')

    except Exception as e:
        return str(e)

    return {'title': product_title, 'rating': product_rating}


# Sử dụng hàm:
urls = [
    'https://www.lazada.vn/products/dien-thoai-samsung-galaxy-a03s-2sim-ram-4g64g-chinh-hang-man-hinh-pls-lcd65hd-bao-hanh-12-thang-i2197657771.html',
    'https://www.lazada.vn/products/dien-thoai-samsung-galaxy-a54-5g-hang-chinh-hang-i2423475974.html',
    'https://www.lazada.vn/products/apple-iphone-15-plus-128gb-chinh-hang-vna-i2417162029.html',
    'https://www.lazada.vn/products/dien-thoai-samsung-galaxy-ultra-i2161334484.html',
    'https://www.lazada.vn/products/xiaomi-note-3-pro-dien-thoai-xiaomi-redmi-note-3-pro-2sim-ram-216g-may-chinh-hang-dien-thoai-cam-ung-cao-cap-gia-re-bao-hanh-12-thang-i2304073512.html']

products = list()

for url in urls:
    product = get_product_info(url)

    products.append(product)

print(products, len(products))