<script>
  const host = window.location.hostname;
  const api = 'http://localhost:5000/api'
  const account = {
    welcome: `${api}/account/welcome`,
  };

  export default {
    host,
    account
  }
</script>
