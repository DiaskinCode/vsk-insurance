<template>
  <component
    :is="component"
    :id="id"
    class="app-input w-100 bg-w bs-2 br-15 p-20 fs-16 b-1 bc-w"
    :type="type"
    :value="value"
    v-bind="$attrs"
    v-on="$listeners"
  />
</template>

<script>
export default {
  name: 'AppInput',
  props: {
    type: {
      type: String,
      default: 'text',
    },
    value: {
      type: [String, Number],
      default: '',
    },
    id: {
      type: String,
      required: true,
    },
    component: {
      type: String,
      required: true,
    },
  },
  data: () => ({
  }),
  computed: {},
  methods: {
  },

}
</script>

<style lang="scss">
.app-input {
  padding-top: 1.8rem;
  padding-bottom: 1.8rem;
  transition: background-color 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
  &.error {
    border-color: #f44336;
    margin-bottom: 6px;
    box-shadow: 0 0 0.3rem rgba(255, 0, 0, 0.4);
  }
  & > * {
    width: 100%;
  }
}
</style>
