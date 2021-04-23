<template>
  <div>
    <h1>Contacto</h1>
    <h2>{{ getNombre }}</h2>
    <v-btn @click="AddCounters">Contar</v-btn>
    <h3>Contador: {{ getCounter }}</h3>
  </div>
</template>

<script>
export default {
  components: {
  },
  computed: {
    getNombre(){
      return this.$store.getters['getName']
    },
    getCounter(){
      return this.$store.getters['getCounter']
    }
  },
  methods: {
    AddCounters(){
      this.$store.commit('addCounter')
    }
  },

}
</script>
