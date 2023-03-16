export default {
  props: {},
  data: () => ({
  }),
  computed: {},
  methods: {
    // 01.02.2021 -> 2023-02-01
    ruDateToISO(date) {
      return date.split('.').reverse().join('-');
    },
  },
}
