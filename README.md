# Access chat server from k8s
kubectl port-forward deployment/py-chat 8080:8080

# Separate terminal run this:

python client.py or python3 client.py