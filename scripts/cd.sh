helm upgrade --install hw-a ./charts/helloworld -f ./charts/helloworld/values_customer_a.yaml && \
helm upgrade --install hw-b ./charts/helloworld -f ./charts/helloworld/values_customer_b.yaml 

