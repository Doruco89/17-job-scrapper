class Product:
    # """상품 정보를 관리하는 클래스"""
 
    def __init__(self, product_id, name, price, weight, stock):
        # """
        # Parameters:
        # product_id (str): 상품 ID
        # name (str): 상품명
        # price (int): 가격
        # weight (float): 무게(kg)
        # stock (int): 재고 수량
        # """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.weight = weight
        self.stock = stock
 
    def get_info(self):
        # """상품 정보를 딕셔너리로 반환"""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "weight": self.weight,
            "stock": self.stock,
        }
 
    def update_stock(self, quantity):
        # """
        # 재고 수량 업데이트
        # 재고가 부족하면 False 반환, 성공하면 True 반환
        # """
        if self.stock < quantity:
            return False
        self.stock -= quantity
        return True
 
    def apply_discount(self, discount_rate):
        # """할인율을 적용한 가격 반환 (원본 가격은 유지)"""
        return int(self.price * (1 - discount_rate))
 
 
class ShoppingCart:
    # """장바구니를 관리하는 클래스"""
 
    def __init__(self):
        # """장바구니 초기화 (상품 목록을 저장할 리스트 생성)"""
        self.items = []
 
    def add_product(self, product, quantity):
        # """
        # 장바구니에 상품 추가
        # {'product': Product객체, 'quantity': 수량} 형태로 저장
        # """
        self.items.append({"product": product, "quantity": quantity})
 
    def remove_product(self, product_id):
        # """상품 ID로 장바구니에서 상품 제거"""
        for item in self.items:
            if item["product"].product_id == product_id:
                self.items.remove(item)
                return True
        return False
 
    def get_total_price(self):
        # """장바구니 내 모든 상품의 총 금액 계산"""
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total
 
    def get_total_weight(self):
        # """장바구니 내 모든 상품의 총 무게 계산"""
        total = 0
        for item in self.items:
            total += item["product"].weight * item["quantity"]
        return total
 
    def show_cart(self):
        # """
        # 장바구니 내용을 보기 좋게 출력
        # 각 상품의 이름, 수량, 가격 표시
        # """
        print("=" * 35)
        print("장바구니")
        print("=" * 35)
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity
            print(f"{product.name} x {quantity}개 = {subtotal:,}원")
        print("-" * 35)
        print(f"총 금액: {self.get_total_price():,}원")
        print(f"총 무게: {self.get_total_weight()}kg")
        print("=" * 35)
 
 
class Order:
    # """주문 정보를 관리하는 클래스"""
    def __init__(self, order_id, cart, customer_name):
        # """
        # Parameters:
        # order_id (str): 주문 ID
        # cart (ShoppingCart): 장바구니 객체
        # customer_name (str): 고객명
        # """
        self.order_id = order_id
        self.cart = cart
        self.customer_name = customer_name
 
    def calculate_final_price(self):
        # """
        # 최종 결제 금액 계산 (상품 금액 + 배송비)
        # 최종 결제 금액 계산 (할인 적용된 상품금액 + 배송비)
        # """
        total = 0
        shipping_fee = 3000
        for item in self.cart.items:
            total += item["product"].apply_discount(0.1) * item["quantity"]    
            # 상품별 할인가(10%) x 수량을 누적
        return total + shipping_fee
            # 전체가격에 배송비 3000원을 합산
        # """
        # 최종 결제 금액 계산 (상품 금액 + 배송비)
        # """
       
    def print_receipt(self):
        #   """
        # 주문서 출력
        # - 주문 ID
        # - 고객명
        # - 주문 상품 목록
        # - 상품 금액
        # - 배송비
        # - 최종 결제 금액
        # """
     
        product_price = self.cart.get_total_price()
        shipping_fee = 3000
 
        print("=" * 35)
        print("주문서")
        print("=" * 35)
        print(f"주문 ID: {self.order_id}")
        print(f"고객명: {self.customer_name}")
        print("-" * 35)
        print("[주문 상품]")
        for item in self.cart.items:
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity
            print(f"  {product.name} x {quantity}개 = {subtotal:,}원")
        print("-" * 35)
        print(f"상품 금액: {product_price:,}원")
        print(f"배송비: {shipping_fee:,}원")
        print(f"최종 결제 금액: {self.calculate_final_price():,}원")        
        print("=" * 35)
 
 
# ----------------- 실행 예시 -----------------
if __name__ == "__main__":
    # 상품 생성
    laptop = Product("P001", "노트북", 1200000, 2.5, 10)
    mouse = Product("P002", "무선마우스", 35000, 0.2, 50)
    keyboard = Product("P003", "기계식키보드", 89000, 1.0, 30)
 
    # 장바구니 생성 및 상품 추가
    cart = ShoppingCart()
    cart.add_product(laptop, 1)
    cart.add_product(mouse, 2)
    cart.add_product(keyboard, 1)
 
    # 장바구니 확인
    cart.show_cart()
    print()
 
    # 주문 생성
    order = Order("ORD20260211001", cart, "홍길동")
 
    # 주문서 출력
    order.print_receipt()