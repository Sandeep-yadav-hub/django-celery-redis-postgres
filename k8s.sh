kind delete clusters app-clusters
kind create cluster --config=kind-deploy.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
cd ./postgresql
kubectl apply -f .
cd ../pgpool
kubectl apply -f .
cd ../pgadmin
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller 
  
# run after ingress is up and running
# kubectl apply -f .



