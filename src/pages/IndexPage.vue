<template>
  <q-page class="row items-center justify-evenly">
    <q-ajax-bar
      ref="bar"
      position="bottom"
      color="accent"
      size="10px"
      skip-hijack
    />
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
          :disable="getting"
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
var getting = ref(false);
const bar = ref(null);

function SendToGpt(msg: string) {
  getting.value = true;
  const barRef = bar.value;
  barRef.start();
  api.post('', msg).then((resp) => {
    console.log(resp);
    responseText.value = resp.data as string;
    getting.value = false;
    const barRef = bar.value;
    if (barRef) {
      barRef.stop();
    }
  });
}
</script>
