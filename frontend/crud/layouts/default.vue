<template>
  <v-app dark>
    <v-main>
      <Navbar/>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'
export default {
  components:{
    Navbar
  }
}
</script>
