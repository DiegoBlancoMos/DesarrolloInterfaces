package com.example.footballplayers.viewmodels;

import android.app.Application;
import android.text.TextUtils;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import com.example.footballplayers.models.User;
import com.example.footballplayers.repositories.UserRepository;

public class RegisterViewModel extends AndroidViewModel {

    private MutableLiveData<String> errorMessage = new MutableLiveData<>();
    private UserRepository userRepository;

    public RegisterViewModel(Application application) {
        super(application);
        userRepository = new UserRepository();
    }

    // Método para validar los datos del formulario
    public boolean validateInputs(String name, String email, String password, String confirmPassword,
                                  String phone, String address) {
        if (TextUtils.isEmpty(name) || TextUtils.isEmpty(email) || TextUtils.isEmpty(password) ||
                TextUtils.isEmpty(confirmPassword) || TextUtils.isEmpty(phone) || TextUtils.isEmpty(address)) {
            errorMessage.setValue("Todos los campos son obligatorios");
            return false;
        }

        if (!password.equals(confirmPassword)) {
            errorMessage.setValue("Las contraseñas no coinciden");
            return false;
        }

        return true;
    }

    // Método para registrar al usuario
    public void registerUser(String name, String email, String password, String phone, String address) {
        User user = new User(name, email, phone, address);

        userRepository.registerUser(email, password, user, new UserRepository.UserRepositoryCallback() {
            @Override
            public void onSuccess() {
                errorMessage.setValue("Usuario registrado exitosamente");
            }

            @Override
            public void onFailure(String error) {
                errorMessage.setValue(error);
            }
        });
    }

    // LiveData para los mensajes de error
    public LiveData<String> getErrorMessage() {
        return errorMessage;
    }
}
