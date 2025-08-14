### Access chat server from k8s:
$ kubectl port-forward deployment/py-chat 8080:8080

### Run client python script:
$ python client.py

or

$ python3 client.py