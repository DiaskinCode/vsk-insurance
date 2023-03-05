<template>
  <div
    class="app-checkbox d-f"
  >
    <Checkbox
      :id="id"
      :value="valueLabel"
      :model-value="value"
      :binary="binary"
      :class="classCheckbox"
      v-bind="$attrs"
      v-on="$listeners"
    />
    <slot>
      <div v-if="label">
        {{ label }}
      </div>
    </slot>
  </div>
</template>

<script>
export default {
  name: 'AppCheckbox',
  props: {
    value: {
      type: [Boolean, Array],
      required: true,
    },
    valueLabel: {
      type: [String, Number],
      default: undefined,
    },
    label: {
      type: [String, Number],
      default: '',
    },
    classCheckbox: {
      type: [String, Object, Array],
      default: '',
    },
    id: {
      type: String,
      required: true,
    },
    binary: {
      type: Boolean,
      default: false,
    },
  },
  data: () => ({
  }),
  computed: {
  },
  methods: {
  },
};
</script>

<style lang="scss">
.app-checkbox {
  .p-checkbox {
    width: 2.4rem;
    height: 2.4rem;
    @media (max-width: 600px) {
      width: 3rem;
      height: 3rem;
    }
  }
  .p-checkbox .p-checkbox-box {
    border: 2px solid #ced4da;
    background: #ffffff;
    width: 2.4rem;
    height: 2.4rem;
    color: #495057;
    border-radius: 1rem;
    transition: background-color 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
    @media (max-width: 600px) {
      width: 3rem;
      height: 3rem;
      border-radius: 1.2rem;
    }
  }
  .p-checkbox .p-checkbox-box .p-checkbox-icon {
    transition-duration: 0.2s;
    color: #ffffff;
    font-size: 1.6rem;
    @media (max-width: 600px) {
      font-size: 1.8rem;
    }
  }
  .p-checkbox .p-checkbox-box.p-highlight {
    border-color: $primary;
    background: $primary;
  }
  .p-checkbox:not(.p-checkbox-disabled) .p-checkbox-box:hover {
    border-color: #2196F3;
  }
  .p-checkbox:not(.p-checkbox-disabled) .p-checkbox-box.p-focus {
    outline: 0 none;
    outline-offset: 0;
    box-shadow: 0 0 0 0.2rem #a6d5fa;
    border-color: #2196F3;
  }
  .p-checkbox:not(.p-checkbox-disabled) .p-checkbox-box.p-highlight:hover {
    border-color: $primary;
    background: $primary;
    color: #ffffff;
  }
  .p-checkbox.p-invalid > .p-checkbox-box {
    border-color: #f44336;
  }
}
</style>
