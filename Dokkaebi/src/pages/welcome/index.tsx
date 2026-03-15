import LoginModal from '@/src/components/loginModal';
import { HeaderTitle } from '@react-navigation/elements';
import { useState } from 'react';
import { Button, StyleSheet, Text, View } from 'react-native';

export type Props = {
  name: string;
};

function Welcome({ name }: Props) {
  const [isOpen, setIsOpen] = useState(false);

  function changeModal(){
  setIsOpen(!isOpen)
}

  return (
    <View style={styles.container}>
      <View style={styles.greeting}>
        <HeaderTitle>Dokkaebi</HeaderTitle>
        <Button
          title="Entrar"
          color="orange"
          onPress={changeModal}
        />
        <LoginModal isOpen={isOpen} onClose={changeModal}></LoginModal>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  greeting: {
    fontSize: 20,
    fontWeight: 'bold',
    margin: 16,
  },
});

export default Welcome;