import { HeaderTitle } from '@react-navigation/elements';
import {Button, StyleSheet, Text, View} from 'react-native';

export type Props = {
  name: string;
};

function Welcome({name} : Props) {


  return (
    <View style={styles.container}>
      <View style={styles.greeting}>
        <HeaderTitle>Dokkaebi</HeaderTitle>
        <Button
          title="Entrar"
          color="orange"
        />
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