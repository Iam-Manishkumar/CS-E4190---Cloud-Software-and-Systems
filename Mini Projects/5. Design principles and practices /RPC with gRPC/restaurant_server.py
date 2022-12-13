import sys
import grpc
from concurrent import futures
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc


RESTAURANT_ITEMS_DRINK = ["fizzy drink", "water", "smoothie", "juice", "beer", "coffee"]
RESTAURANT_ITEMS_DESSERT = ["ice cream", "chocolate cake", "cheese cake", "brownie", "pancakes", "waffles"]
RESTAURANT_ITEMS_FOOD = ["fish", "chips", "burger", "pizza", "pasta", "salad"]



class Restaurant(restaurant_pb2_grpc.RestaurantServicer):
    # Logic goes here

    def DessertOrder(self, request, context):
        itemCount = 0
        for item in request.items:
            if item not in RESTAURANT_ITEMS_DESSERT:
                return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID, 
                    status=restaurant_pb2.RestaurantResponse .REJECTED
                    )
            elif item in RESTAURANT_ITEMS_DESSERT:
                itemCount = itemCount + 1

        if itemCount == len(request.items):
            return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID, 
                    status=restaurant_pb2.RestaurantResponse.ACCEPTED
                    )
        else:
            return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID, 
                    status=restaurant_pb2.RestaurantResponse .REJECTED
                    )
    def FoodOrder(self, request, context):
        itemCount = 0
        for item in request.items:
            if item not in RESTAURANT_ITEMS_FOOD:
                return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID, 
                    status=restaurant_pb2.RestaurantResponse .REJECTED
                    )
            # elif item in RESTAURANT_ITEMS_FOOD:
            # elif item in RESTAURANT_ITEMS_FOOD:
            # elif item in RESTAURANT_ITEMS_FOOD:
            # elif item in RESTAURANT_ITEMS_FOOD:
            # elif item in RESTAURANT_ITEMS_FOOD:

            else:
                itemCount = itemCount + 1

        if itemCount == len(request.items):
            return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID, 
                    status=restaurant_pb2.RestaurantResponse.ACCEPTED
                    )
        else:
            return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID, 
                    status=restaurant_pb2.RestaurantResponse.REJECTED
                    )        
                            
    def DrinkOrder(self, request, context):
        itemCount = 0
        for item in request.items:
            if item not in RESTAURANT_ITEMS_DRINK:
                return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID, 
                    status=restaurant_pb2.RestaurantResponse.REJECTED
                    )
            elif item in RESTAURANT_ITEMS_DRINK:
                itemCount = itemCount + 1

        if itemCount == len(request.items):
            return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID, 
                    status=restaurant_pb2.RestaurantResponse.ACCEPTED
                    )
        else:
            return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID, 
                    status=restaurant_pb2.RestaurantResponse #.REJECTED
                    )

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2 ))
    restaurant_pb2_grpc.add_RestaurantServicer_to_server(
    Restaurant(), server)
    server.add_insecure_port('[::]:'+ sys.argv[1])# + '50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()