# supervisionado

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# Dados de exemplo

x_train = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y_train = tf.constant([[2.0], [4.0], [6.0], [8.0]])

# Definimos os dados de exemplo x_train (entradas) e y_train (saídas desejadas) para treinar o modelo.
# No exemplo, estamos usando pares de entrada e saída que representam uma relação linear simples (o dobro das entradas).

# Modelo de Regressão Linear Simples

model = Sequential()
model.add(Dense(units=1, input_shape=(1,)))
model.compile(optimizer="sgd", loss="mean_squared_error")

# Definimos o modelo de Regressão Linear Simples usando a API Keras Sequential.
# O modelo consiste em uma única camada densa (ou totalmente conectada) com um neurônio (ou unidade) e uma entrada.
# Estamos usando a função de perda(loss) de erro quadrático médio (mean squared error - 'mean_squared_error') e o otimizador 'sgd' (descida de gradiente estocástica)

# Treinamento do modelo

history = model.fit(x_train, y_train, epochs=1000, verbose=0)

# Nesta seção, treinamos o modelo usando os dados de exemplo.
# Executamos 1000 épocas de treinamento (epochs) e armazenamos o histórico de treinamento em history.
# O argumento verbose=0 faz com que o treinamento seja executado em modo silencioso, sem exibir informações de progresso.

# Previsão

X_new = tf.constant([[5.0]])
prediction = model.predict(X_new)
print("Predição:", prediction[0][0])

# Aqui, fazemos uma previsão usando o modelo trienado.
# Informamos uma nova entrada X_new (5.0) e calculamos a previsão. O resultado é impresso na tela.

# Plotar os resultados

plt.plot(history.history["loss"])
plt.title("Model Loss Over Training")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()

# Por fim, plotamos a perda (loss) do modelo ao longo do treinamento. Usamos o history.history['loss'] para obter a lista das perdas em cada época.
# Configuramos o título e rótulos dos eixos e exibimos o gráficos com plt.show().
# Isso nos permite visualizar como a perda do modelo diminuiu durante o treinamento, o que é uma indicação do aprendizado do modelo.

##############################################
# Não supervisionada

import tensorflow as tf

from tensorflow.keras.layers import Input, Dense

from tensorflow.keras.models import Model


# Dados de exemplo

X_unsupervised = tf.constant([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]])


# Modelo Autoencoder Simples

input_layer = Input(shape=(2,))

encoded = Dense(units=1)(input_layer)

decoded = Dense(units=2)(encoded)


autoencoder = Model(inputs=input_layer, outputs=decoded)

autoencoder.compile(optimizer="adam", loss="mean_squared_error")


# Treinamento do modelo não supervisionado

autoencoder.fit(X_unsupervised, X_unsupervised, epochs=1000, verbose=0)


# Previsão

prediction_unsupervised = autoencoder.predict(X_unsupervised)

print("Predição Não Supervisionada:", prediction_unsupervised)

#######################################################

# Por reforço

import tensorflow as tf

import gym


# Ambiente CartPole do Gym

env = gym.make("CartPole-v1")


# Modelo Simples para Aprendizado por Reforço

model_reinforcement = tf.keras.Sequential(
    [
        tf.keras.layers.Dense(
            24, activation="relu", input_shape=(env.observation_space.shape[0],)
        ),
        tf.keras.layers.Dense(env.action_space.n, activation="linear"),
    ]
)


model_reinforcement.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss="mse"
)


# Treinamento por Reforço (exemplo fictício)

max_episodes = 1000  # Defina o número máximo de episódios

for episode in range(max_episodes):

    state = env.reset()

    done = False

    while not done:

        action = env.action_space.sample()

        next_state, reward, done, _ = env.step(action)

        target = reward + 0.95 * tf.reduce_max(
            model_reinforcement.predict(next_state.reshape(1, -1))
        )

        target_f = model_reinforcement.predict(state.reshape(1, -1))

        target_f[0][action] = target

        model_reinforcement.fit(state.reshape(1, -1), target_f, epochs=1, verbose=0)

        state = next_state

    # Condição de parada

    if episode % 10 == 0:

        average_reward = sum(reward for _ in range(10)) / 10.0

        print(f"Episode {episode}, Average Reward: {average_reward}")

        # Adicionando uma condição de parada

        if average_reward == 1:  # Pode ajustar esse valor conforme necessário

            print(f"Solved after {episode} episodes!")

            break
