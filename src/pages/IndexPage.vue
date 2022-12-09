<template>
  <q-page class="row items-center justify-evenly">
    <div class="q-pa-md" style="min-width: 75%">
      <q-input
        class="q-pa-md"
        label="chat with gpt"
        v-model="inputText"
        filled
        autogrow
      />
      <div class="q-pa-md" style="text-align: center">
        <q-btn
          class=""
          color="primary"
          label="Send to gpt"
          @click="SendToGpt(inputText)"
        />
      </div>
      <q-input
        class="q-pa-md"
        label="response from gpt"
        v-model="responseText"
        filled
        autogrow
        :readonly="true"
      />
    </div>
  </q-page>
</template>

<script setup lang="ts">
// import { Todo, Meta } from 'components/models';
// import ExampleComponent from 'components/ExampleComponent.vue';
import { ref } from 'vue';
import { api } from 'boot/axios';
var inputText = ref('');
var responseText = ref('');

function SendToGpt(msg: string) {
  api.post('', msg).then((resp) => {
    console.log(resp);
    responseText.value = resp.data as string;
  });
}
</script>
