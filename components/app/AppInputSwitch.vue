<template>
  <div class="app-switch d-f ai-c">
    <InputSwitch
      :id="id"
      class=""
      :class="classInner"
      :value="value"
      v-bind="$attrs"
      v-on="$listeners"
    >
    </InputSwitch>
    <slot>
      <label
        :for="id"
        class="ml-10 us-n"
        @click="updateValue"
      >
        {{ label }}
      </label>
    </slot>
  </div>
</template>

<script>
export default {
  name: 'AppInputSwitch',
  props: {
    value: {
      type: Boolean,
      required: true,
    },
    id: {
      type: String,
      required: true,
    },
    label: {
      type: [String, Number],
      default: '',
    },
    classInner: {
      type: [String, Object, Array],
      default: '',
    },
  },
  data: () => ({
  }),
  computed: {},
  methods: {
    updateValue() {
      this.$emit('input', !this.value);
    },
  },
}
</script>

<style lang="scss">
.app-switch {
  .p-inputswitch {
    width: 4.2rem;
    height: 2.4rem;
  }
  .p-inputswitch .p-inputswitch-slider {
    background: #ced4da;
    transition: background-color 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
    border-radius: 1.6rem;
  }
  .p-inputswitch .p-inputswitch-slider:before {
    background: #ffffff;
    width: 2rem;
    height: 2rem;
    left: 0.25rem;
    margin-top: -1rem;
    border-radius: 50%;
    transition-duration: 0.2s;
  }
  .p-inputswitch.p-inputswitch-checked .p-inputswitch-slider:before {
    transform: translateX(1.6rem);
  }
  .p-inputswitch.p-focus .p-inputswitch-slider {
    outline: 0 none;
    outline-offset: 0;
    box-shadow: 0 0 0 0.2rem #a6d5fa;
  }
  .p-inputswitch:not(.p-disabled):hover .p-inputswitch-slider {
    background: #b6bfc8;
  }
  .p-inputswitch.p-inputswitch-checked .p-inputswitch-slider {
    background: #2196F3;
  }
  .p-inputswitch.p-inputswitch-checked .p-inputswitch-slider:before {
    background: #ffffff;
  }
  .p-inputswitch.p-inputswitch-checked:not(.p-disabled):hover .p-inputswitch-slider {
    background: #0d89ec;
  }
  .p-inputswitch.p-invalid {
    border-color: #f44336;
  }
}
</style>
