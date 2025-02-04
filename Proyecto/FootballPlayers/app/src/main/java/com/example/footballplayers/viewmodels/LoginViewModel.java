package com.example.footballplayers.viewmodels;

import android.app.Application;
import android.text.TextUtils;
import android.util.Patterns;

import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.annotation.NonNull;

import com.example.footballplayers.repositories.UserRepository;

public class LoginViewModel extends AndroidViewModel {

    private final MutableLiveData<String> errorMessage = new MutableLiveData<>();
    private final MutableLiveData<Boolean> isLoading = new MutableLiveData<>();
    private final MutableLiveData<Boolean> navigateToDashboard = new MutableLiveData<>();
    private final UserRepository userRepository;

    public LoginViewModel(@NonNull Application application) {
        super(application);
        userRepository = new UserRepository();
        isLoading.setValue(false);
    }

    // Método para validar el email
    private boolean isEmailValid(String email) {
        return Patterns.EMAIL_ADDRESS.matcher(email).matches();
    }

    // Método para validar la contraseña (mínimo 6 caracteres)
    private boolean isPasswordValid(String password) {
        return password.length() >= 6;
    }

    // Método para validar los inputs
    public boolean validateInputs(String email, String password) {
        if (TextUtils.isEmpty(email) || TextUtils.isEmpty(password)) {
            errorMessage.setValue("Por favor, completa todos los campos");
            return false;
        }

        if (!isEmailValid(email)) {
            errorMessage.setValue("Por favor, ingresa un email válido");
            return false;
        }

        if (!isPasswordValid(password)) {
            errorMessage.setValue("La contraseña debe tener al menos 6 caracteres");
            return false;
        }

        return true;
    }

    // Método para iniciar sesión
    public void loginUser(String email, String password) {
        if (!validateInputs(email, password)) {
            return;
        }

        isLoading.setValue(true);
        userRepository.loginUser(email, password, new UserRepository.UserRepositoryCallback() {
            @Override
            public void onSuccess() {
                isLoading.postValue(false);
                navigateToDashboard.postValue(true);
            }

            @Override
            public void onFailure(String error) {
                isLoading.postValue(false);
                errorMessage.postValue(error);
            }
        });
    }

    // Método para limpiar la navegación después de usarla
    public void onNavigationComplete() {
        navigateToDashboard.setValue(false);
    }

    // LiveData para los mensajes de error
    public LiveData<String> getErrorMessage() {
        return errorMessage;
    }

    // LiveData para el estado de carga
    public LiveData<Boolean> getIsLoading() {
        return isLoading;
    }

    // LiveData para la navegación
    public LiveData<Boolean> getNavigateToDashboard() {
        return navigateToDashboard;
    }

    // Método para limpiar los mensajes de error
    public void clearError() {
        errorMessage.setValue(null);
    }

    @Override
    protected void onCleared() {
        super.onCleared();
        // Limpieza de recursos si es necesario
    }
}