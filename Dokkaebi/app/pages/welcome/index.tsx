import Message from '@/src/components/message';
import { useState } from 'react';
import { Button, StyleSheet, Text, TextInput, View, TouchableOpacity } from 'react-native';
import axios from 'axios';
import { router } from 'expo-router';

export type Props = {
  name: string;
};

function Welcome({ name }: Props) {
  const [isOpen, setIsOpen] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState('');

  function changeModal() {
    setIsOpen(!isOpen)
  }

  async function login() {
    axios.post('http://localhost:8000/auth/login', {
      username,
      password
    }).then((result) => {
      router.replace("/pages/dashboard");
    }).catch((err) => {
      // setMessage(err.response.data.message)
      changeModal()
    });
  }

  return (
    <View style={styles.container}>
      <View style={styles.card}>
        <Text style={styles.brand}>Dokkaebi</Text>

        <View style={styles.inputContainer}>
          <TextInput
            placeholder='Login'
            placeholderTextColor="#888"
            style={styles.input}
            value={username}
            onChangeText={setUsername}
          />
          <TextInput
            placeholder='Password'
            placeholderTextColor="#888"
            secureTextEntry={true}
            style={styles.input}
            value={password}
            onChangeText={setPassword}
          />
        </View>

        <TouchableOpacity style={styles.button} onPress={login}>
          <Text style={styles.buttonText}>Entrar</Text>
        </TouchableOpacity>

        <Message
          isShown={isOpen}
          onClose={changeModal}
          duration={2}
          message={message}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f0f0f',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  card: {
    width: '100%',
    maxWidth: 400,
    backgroundColor: '#1a1a1a', // Cinza muito escuro
    borderRadius: 16,
    padding: 30,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 10,
  },
  brand: {
    fontSize: 32,
    fontWeight: '900',
    color: 'orange',
    marginBottom: 40,
    letterSpacing: 2,
    textTransform: 'uppercase',
  },
  inputContainer: {
    width: '100%',
    gap: 12,
    marginBottom: 25,
  },
  input: {
    width: '100%',
    backgroundColor: '#2a2a2a',
    color: '#fff',
    padding: 16,
    borderRadius: 8,
    fontSize: 16,
    borderWidth: 1,
    borderColor: '#333',
  },
  button: {
    width: '100%',
    backgroundColor: 'orange',
    padding: 16,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 10,
  },
  buttonText: {
    color: '#000',
    fontSize: 18,
    fontWeight: 'bold',
  },
});

export default Welcome;