package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

//structs

type HealthResponse struct {
	Status string `json:"status"`
}
type HomeResponse struct {
	Message string `json:"status"`
}

func main() {
	// routes
	http.HandleFunc("/", home)
	http.HandleFunc("/health", health)

	fmt.Println("Dokkaebi iniciado")
	err := http.ListenAndServe("127.0.0.1:8000", nil)

	if err != nil {
		fmt.Println("Erro ao iniciar servidor", err)
	}
}

func home(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	response := HomeResponse{
		Message: "Dokkaebi node está funcionando!",
	}

	json.NewEncoder(w).Encode(response)
}

func health(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	response := HealthResponse{
		Status: "online",
	}

	json.NewEncoder(w).Encode(response)
}
