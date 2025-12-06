from services.converter import convert_yaml_to_provider

yaml_file = """
apiVersion: v1
kind: Service
metadata:
  name: myapp
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
spec:
  type: LoadBalancer
  ports:
    - port: 80
"""

converted = convert_yaml_to_provider(yaml_file, "gcp")
print(converted)
