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
  & > * {
    width: 100%;
  }
}
</style>
